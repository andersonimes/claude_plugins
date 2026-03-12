#!/usr/bin/env python3

"""
Claude Code session summarizer.
Reads a conversation transcript JSONL from a SessionEnd hook,
calls `claude -p` to generate a markdown summary, and saves it
to a configurable output directory.
"""

import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# ── Configuration (all overridable via env / config file) ───────────
CONFIG_PATH = Path.home() / ".claude" / "session-summarizer.conf"


def load_config() -> dict:
    """Load key=value config, then let env vars override."""
    cfg = {}
    if CONFIG_PATH.exists():
        for line in CONFIG_PATH.read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                k, v = line.split("=", 1)
                cfg[k.strip()] = v.strip().strip('"').strip("'")
    # Env vars take precedence
    for key in ("OUTPUT_DIR", "USER_NAME", "MODEL"):
        val = os.environ.get(key)
        if val:
            cfg[key] = val
    return cfg


CFG = load_config()

USER_NAME = CFG.get("USER_NAME", "The User")
MODEL = CFG.get("MODEL", "claude-haiku-4-5-20251001")


# ── Transcript parsing ──────────────────────────────────────────────


def extract_messages(transcript_path: str) -> list[dict]:
    """Extract user and assistant text messages from a transcript JSONL."""
    messages = []
    with open(transcript_path) as f:
        for line in f:
            obj = json.loads(line)
            msg_type = obj.get("type", obj.get("role", ""))
            timestamp = obj.get("timestamp", "")

            if msg_type in ("user", "assistant"):
                content = obj.get("message", {})
                if isinstance(content, dict):
                    text = _extract_text(content.get("content", ""))
                else:
                    text = str(content) if content else ""

                if not text and msg_type == "user" and isinstance(obj.get("message"), str):
                    text = obj["message"]

                text = _clean_system_tags(text)
                if text.strip():
                    messages.append(
                        {"role": msg_type, "text": text.strip(), "timestamp": timestamp}
                    )

    return messages


def _extract_text(content) -> str:
    """Extract text from message content (string or list of blocks)."""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for block in content:
            if isinstance(block, dict):
                if block.get("type") == "text":
                    parts.append(block["text"])
                elif block.get("type") == "tool_use":
                    parts.append(f"[Used tool: {block.get('name', 'unknown')}]")
        return "\n".join(parts)
    return ""


def _clean_system_tags(text: str) -> str:
    """Remove system tags and other noise from message text."""
    for tag in (
        "system-reminder",
        "local-command-caveat",
        "local-command-stdout",
        "command-name",
        "command-message",
        "command-args",
        "available-deferred-tools",
    ):
        text = re.sub(rf"<{tag}>.*?</{tag}>", "", text, flags=re.DOTALL)
    return text.strip()


# ── Summarization ───────────────────────────────────────────────────


def slugify(text: str) -> str:
    """Create a URL-friendly slug from text."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text[:60].strip("-")


def summarize(messages: list[dict]) -> list[dict]:
    """Call claude -p to generate session summaries, splitting by topic."""
    transcript_text = ""
    for msg in messages:
        role = USER_NAME if msg["role"] == "user" else "Claude"
        ts = msg.get("timestamp", "")
        ts_prefix = f"[{ts}] " if ts else ""
        text = msg["text"][:2000] + "..." if len(msg["text"]) > 2000 else msg["text"]
        transcript_text += f"{ts_prefix}**{role}:** {text}\n\n"

    if len(transcript_text) > 50000:
        transcript_text = transcript_text[:50000] + "\n\n[transcript truncated]"

    prompt = f"""Analyze this Claude Code session transcript. The session may cover multiple distinct topics or tasks. If the user changed subjects to something not strongly related to the original task, split those into separate summaries.

Each message in the transcript is prefixed with an ISO timestamp. Return a JSON array of objects. Each object represents one topic/task and has these fields:

- "title": A short descriptive title for what was accomplished (5-10 words)
- "timestamp": The ISO timestamp of the first message where this topic begins (copy it exactly from the transcript)
- "summary": 2-3 sentences describing what was done and the outcome. Write in a slightly whimsical, fun tone — like you're telling a friend what they got up to. Refer to the user as "{USER_NAME}" (not "the user"). Keep it light but informative.
- "sample_prompts": An array of 2-4 interesting/representative prompts {USER_NAME} sent during this topic (exact quotes, shortened if very long)
- "tags": An array of 3-6 topic tags (lowercase, e.g. "shell-config", "debugging", "python")
- "links": An array of any relevant URLs that appeared in this part of the conversation (documentation pages, GitHub repos, tools referenced, etc.). Omit internal file paths — only include actual web URLs. If none, use an empty array.

If the whole session is one coherent topic, return an array with a single object. Only split when the topic genuinely changes.

Return ONLY a valid JSON array, no markdown fencing.

<transcript>
{transcript_text}
</transcript>"""

    cmd = ["claude", "-p", "--model", MODEL, "--output-format", "text"]
    result = subprocess.run(
        cmd, input=prompt, capture_output=True, text=True, timeout=120
    )

    if result.returncode != 0:
        print(f"claude -p failed: {result.stderr}", file=sys.stderr)
        sys.exit(1)

    text = result.stdout.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\n?", "", text)
        text = re.sub(r"\n?```$", "", text)
    parsed = json.loads(text)
    if isinstance(parsed, dict):
        parsed = [parsed]
    return parsed


# ── File output ─────────────────────────────────────────────────────


def write_summary(summary: dict, session_id: str, output_dir: Path) -> Path:
    """Write a markdown summary file to the output directory."""
    topic_ts = summary.get("timestamp", "")
    if topic_ts:
        try:
            dt = datetime.fromisoformat(topic_ts.replace("Z", "+00:00"))
        except ValueError:
            dt = datetime.now()
    else:
        dt = datetime.now()

    datetime_str = dt.strftime("%Y-%m-%d %H:%M UTC")
    year_month_dir = output_dir / dt.strftime("%Y") / dt.strftime("%m")
    year_month_dir.mkdir(parents=True, exist_ok=True)

    filename_ts = dt.strftime("%Y-%m-%d-%H%M")
    slug = slugify(summary["title"])
    filename = f"{filename_ts}-{slug}.md"
    filepath = year_month_dir / filename

    counter = 1
    while filepath.exists():
        counter += 1
        filename = f"{filename_ts}-{slug}-{counter}.md"
        filepath = year_month_dir / filename

    tags_str = ", ".join(summary["tags"])
    prompts_str = "\n".join(f'- "{p}"' for p in summary["sample_prompts"])
    links = summary.get("links", [])
    links_str = "\n".join(f"- {url}" for url in links) if links else ""

    content = f"""# {summary["title"]}

**Date:** {datetime_str}
**Session:** `{session_id}`
**Tags:** {tags_str}

## Summary

{summary["summary"]}

## Sample Prompts

{prompts_str}
"""

    if links_str:
        content += f"""
## Links

{links_str}
"""

    filepath.write_text(content)
    return filepath


def purge_session(session_id: str, output_dir: Path):
    """Remove all existing summary files for a given session ID."""
    if not output_dir.exists():
        return
    count = 0
    for md_file in output_dir.rglob("*.md"):
        try:
            text = md_file.read_text()
            if f"**Session:** `{session_id}`" in text:
                md_file.unlink()
                count += 1
        except Exception:
            pass
    if count:
        print(f"Purged {count} old summaries for session {session_id}")


# ── Main ────────────────────────────────────────────────────────────


def main():
    hook_input = json.loads(sys.stdin.read())
    session_id = hook_input.get("session_id", "unknown")
    transcript_path = hook_input.get("transcript_path", "")
    cwd = hook_input.get("cwd", os.getcwd())

    # Resolve output directory: config override, or <project>/session-summaries
    configured_dir = CFG.get("OUTPUT_DIR")
    if configured_dir:
        output_dir = Path(os.path.expanduser(configured_dir))
    else:
        output_dir = Path(cwd) / "session-summaries"

    if not transcript_path or not Path(transcript_path).exists():
        print(f"No transcript found at {transcript_path}", file=sys.stderr)
        sys.exit(1)

    messages = extract_messages(transcript_path)
    if len(messages) < 2:
        print("Session too short to summarize", file=sys.stderr)
        sys.exit(0)

    purge_session(session_id, output_dir)

    summaries = summarize(messages)
    for summary in summaries:
        filepath = write_summary(summary, session_id, output_dir)
        print(f"Summary written to {filepath}")


if __name__ == "__main__":
    main()
