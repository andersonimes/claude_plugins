# Stay Awake

A [Claude Code](https://docs.anthropic.com/en/docs/claude-code) plugin that prevents your computer from sleeping while a session is active.

## What it does

- **PreToolUse hook**: Starts a sleep inhibitor when Claude first uses a tool. The inhibitor lasts for a configurable timeout (default: 24 hours). Idempotent — if one is already running, it does nothing.
- **Stop hook**: When a session ends, replaces the inhibitor with a shorter grace period (default: 10 minutes) instead of killing it outright.

The grace period exists because of workflows like `/loop` where Claude runs a command every few minutes. Without it, the machine could sleep during the gap between iterations. The grace keeps the inhibitor alive long enough for the next iteration to start, then that session takes over. When you're truly done, the grace expires and normal power management resumes.

### Lifecycle example

```
Session 1 starts
  └─ PreToolUse → start inhibitor (24h timeout)
  └─ ... working ...
  └─ Stop → replace with grace period (10min)

          ← 2 min gap (machine stays awake) →

Session 2 starts (e.g. /loop iteration)
  └─ PreToolUse → inhibitor still running from grace, skip
  └─ ... working ...
  └─ Stop → replace with grace period (10min)

          ← no more sessions →

  └─ Grace expires after 10 min → machine can sleep again
```

## Platform support

| Platform | Method |
|----------|--------|
| Linux (systemd) | `systemd-inhibit` blocks idle and sleep |
| macOS | `caffeinate` blocks display sleep, idle sleep, and system sleep |

## Install

First, add the marketplace (one time):
```
/plugin marketplace add andersonimes/claude_plugins
```

Then install:
```
/plugin install stay-awake@claude_plugins
```

Works out of the box with no configuration.

## Configuration

Create `~/.claude/stay-awake.conf` to customize behavior:

```bash
# How long the inhibitor runs during an active session (in seconds).
# Default: 86400 (24 hours)
TIMEOUT=86400

# How long to keep the machine awake after a session ends (in seconds).
# Bridges the gap between /loop iterations or back-to-back sessions.
# Set to 0 to kill the inhibitor immediately when a session ends.
# Default: 600 (10 minutes)
STOP_GRACE=600
```

### Common configurations

| Use case | `TIMEOUT` | `STOP_GRACE` |
|----------|-----------|--------------|
| Default (24h session, 10min grace) | `86400` | `600` |
| Week-long tasks | `604800` | `600` |
| No grace period (kill on stop) | `86400` | `0` |
| Long grace for slow loops | `86400` | `1800` |

### Environment variable overrides

Environment variables take precedence over the config file:

| Variable | Overrides |
|----------|-----------|
| `STAY_AWAKE_TIMEOUT` | `TIMEOUT` |
| `STAY_AWAKE_STOP_GRACE` | `STOP_GRACE` |

## Uninstall

```bash
claude plugin uninstall stay-awake
```

## License

MIT
