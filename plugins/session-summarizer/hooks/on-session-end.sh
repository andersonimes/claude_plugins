#!/bin/bash
# Hook wrapper for session summarizer.
# Spawns the Python summarizer in the background so the hook
# returns immediately (SessionEnd has a 1.5-second timeout).

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
CONF="$HOME/.claude/session-summarizer.conf"
INPUT=$(cat)

# Check config exists
if [ ! -f "$CONF" ]; then
    echo "[session-summarizer] Config not found. Create $CONF with your settings." >&2
    echo "[session-summarizer] See: https://github.com/andersonimes/claude_plugins/tree/main/plugins/session-summarizer#configuration" >&2
    exit 0
fi

# Source API key from config if not already set
if [ -z "$ANTHROPIC_API_KEY" ]; then
    val=$(grep '^ANTHROPIC_API_KEY=' "$CONF" | head -1 | cut -d= -f2- | tr -d '"' | tr -d "'")
    [ -n "$val" ] && export ANTHROPIC_API_KEY="$val"
fi

echo "$INPUT" | nohup env ANTHROPIC_API_KEY="$ANTHROPIC_API_KEY" \
    uv run --script "$SCRIPT_DIR/summarize-session.py" \
    >> "$HOME/.claude/session-summary.log" 2>&1 &

exit 0
