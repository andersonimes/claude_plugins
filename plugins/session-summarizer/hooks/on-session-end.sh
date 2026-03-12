#!/bin/bash
# Hook wrapper for session summarizer.
# Spawns the Python summarizer in the background so the hook
# returns immediately (SessionEnd has a 1.5-second timeout).

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
INPUT=$(cat)

echo "$INPUT" | nohup python3 "$SCRIPT_DIR/summarize-session.py" \
    >> "$HOME/.claude/session-summary.log" 2>&1 &

exit 0
