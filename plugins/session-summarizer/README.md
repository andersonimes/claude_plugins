# Claude Session Summarizer

A [Claude Code](https://docs.anthropic.com/en/docs/claude-code) plugin that automatically summarizes every session into markdown files when the conversation ends.

## What it does

When a Claude Code session ends, this plugin:

1. Reads the conversation transcript
2. Calls the Claude API to generate a concise, topic-aware summary
3. Saves markdown files organized by `YYYY/MM/` into your chosen directory
4. Splits multi-topic sessions into separate summary files

Each summary includes a title, tags, sample prompts, and any relevant links from the conversation.

## Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) CLI
- [uv](https://docs.astral.sh/uv/) (Python package runner)
- An [Anthropic API key](https://console.anthropic.com/settings/keys)

## Install

First, add the marketplace (one time):
```
/plugin marketplace add andersonimes/claude_plugins
```

Then install:
```
/plugin install session-summarizer@claude_plugins
```

## Configuration

After installing, create `~/.claude/session-summarizer.conf`:

```
ANTHROPIC_API_KEY=sk-ant-...
OUTPUT_DIR=~/claude-sessions
USER_NAME=Alice
MODEL=claude-haiku-4-5-20251001
```

| Parameter | Description | Default |
|-----------|-------------|---------|
| `ANTHROPIC_API_KEY` | Your Anthropic API key | *required* (or set as env var) |
| `OUTPUT_DIR` | Where to save summaries | `~/claude-sessions` |
| `USER_NAME` | How you're referred to in summaries | System username |
| `MODEL` | Claude model for summarization | `claude-haiku-4-5-20251001` |

Environment variables with the same names override the config file.

## Output

Summaries are saved as markdown organized by year and month:

```
claude-sessions/
  2026/
    03/
      2026-03-12-1430-debugging-api-rate-limits.md
      2026-03-12-1505-setting-up-docker-compose.md
```

Each file looks like:

```markdown
# Debugging API Rate Limits

**Date:** 2026-03-12 14:30 UTC
**Session:** `abc123`
**Tags:** debugging, api, python, rate-limiting

## Summary

Alice and Claude tracked down a sneaky rate-limiting bug...

## Sample Prompts

- "why am I getting 429s on the /users endpoint"
- "can you add exponential backoff to the retry logic"
```

## Uninstall

```bash
claude plugin uninstall session-summarizer
```

Your existing summaries and config file are not deleted.

## License

MIT
