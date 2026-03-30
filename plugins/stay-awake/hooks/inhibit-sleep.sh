#!/usr/bin/env bash
# stay-awake: Prevent system sleep while Claude Code is active.
# Supports Linux (systemd-inhibit) and macOS (caffeinate).
#
# Usage: inhibit-sleep.sh {start|stop}
#
#   start  — Called on PreToolUse. Launches or refreshes a sleep inhibitor
#            that lasts TIMEOUT seconds (default: 86400 / 24 hours).
#
#   stop   — Called on session Stop. Replaces the running inhibitor with a
#            shorter STOP_GRACE timeout (default: 600 / 10 minutes). This
#            keeps the machine awake across gaps between sessions (e.g.
#            /loop intervals) without leaving it inhibited forever.
#            Set STOP_GRACE=0 to kill the inhibitor immediately on stop.
#
# Configuration: ~/.claude/stay-awake.conf (sourced as bash)
#   TIMEOUT      — Inhibit duration in seconds (default: 86400)
#   STOP_GRACE   — Grace period in seconds after session ends (default: 600)
#                  Set to 0 to disable (kill immediately on stop)
#
# Environment variables with the same names override the config file.

set -euo pipefail

PIDFILE="/tmp/claude-stay-awake.pid"
ACTION="${1:-start}"

# ── Defaults ──────────────────────────────────────────────────────────
TIMEOUT=86400    # 24 hours
STOP_GRACE=600   # 10 minutes

# ── Load config ──────────────────────────────────────────────────────
CONF="$HOME/.claude/stay-awake.conf"
if [ -f "$CONF" ]; then
  # shellcheck source=/dev/null
  source "$CONF"
fi

# Environment variable overrides
TIMEOUT="${STAY_AWAKE_TIMEOUT:-$TIMEOUT}"
STOP_GRACE="${STAY_AWAKE_STOP_GRACE:-$STOP_GRACE}"

# ── Helpers ──────────────────────────────────────────────────────────

is_running() {
  [ -f "$PIDFILE" ] && kill -0 "$(cat "$PIDFILE")" 2>/dev/null
}

kill_inhibitor() {
  if is_running; then
    kill "$(cat "$PIDFILE")" 2>/dev/null || true
    rm -f "$PIDFILE"
  fi
}

# Start a new inhibitor process for the given duration (in seconds).
# Kills any existing inhibitor first so the timer resets.
start_inhibitor() {
  local duration="$1"
  kill_inhibitor

  if [[ "$OSTYPE" == darwin* ]]; then
    caffeinate -dims -t "$duration" &
    echo $! > "$PIDFILE"
  elif command -v systemd-inhibit &>/dev/null; then
    systemd-inhibit --what=idle:sleep \
      --who="Claude Code" \
      --why="Active session" \
      --mode=block \
      sleep "$duration" &
    echo $! > "$PIDFILE"
  fi
}

# ── Actions ──────────────────────────────────────────────────────────

do_start() {
  # Idempotent: if an inhibitor is already running, leave it alone.
  # This avoids resetting the timer on every single tool call.
  if is_running; then
    exit 0
  fi
  start_inhibitor "$TIMEOUT"
}

do_stop() {
  if [ "$STOP_GRACE" -eq 0 ]; then
    # Grace disabled — kill immediately
    kill_inhibitor
  else
    # Replace the long-running inhibitor with a short grace period.
    # If another session starts before it expires, do_start will find
    # it still running and leave it alone. When that session's first
    # tool fires, the inhibitor is already active. On *that* session's
    # stop, the grace resets again — so chained sessions (or /loop
    # iterations) keep the machine awake continuously.
    start_inhibitor "$STOP_GRACE"
  fi
}

# ── Main ─────────────────────────────────────────────────────────────

case "$ACTION" in
  start) do_start ;;
  stop)  do_stop  ;;
  *)     echo "Usage: $0 {start|stop}" >&2; exit 1 ;;
esac
