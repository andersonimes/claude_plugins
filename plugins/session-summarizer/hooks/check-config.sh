#!/bin/bash
# SessionStart hook: warn if config is missing.
# stdout from SessionStart hooks is injected into Claude's context.

CONF="$HOME/.claude/session-summarizer.conf"

if [ ! -f "$CONF" ]; then
    cat <<'EOF'
[session-summarizer] The session summarizer plugin is installed but not configured.
Create ~/.claude/session-summarizer.conf with the following settings:

ANTHROPIC_API_KEY=sk-ant-...
OUTPUT_DIR=~/claude-sessions
USER_NAME=YourName
MODEL=claude-haiku-4-5-20251001

Sessions will not be summarized until this file exists.
EOF
fi

exit 0
