# Claude Code Plugin Marketplace

A collection of plugins for [Claude Code](https://docs.anthropic.com/en/docs/claude-code).

## Setup

Add this marketplace to Claude Code:

```
/plugin marketplace add andersonimes/claude_plugins
```

Then install plugins by name:

```
/plugin install <plugin-name>@claude_plugins
```

## Plugins

### [session-summarizer](plugins/session-summarizer/)

Automatically summarizes every Claude Code session into markdown files when the conversation ends. Splits multi-topic sessions, includes tags, sample prompts, and relevant links.

```
/plugin install session-summarizer@claude_plugins
```

Works out of the box with zero config. Summaries are saved to `session-summaries/` in your project directory by default. See the [plugin README](plugins/session-summarizer/README.md) for optional overrides.

### [stay-awake](plugins/stay-awake/)

Prevents your computer from sleeping while a Claude Code session is active. Uses `systemd-inhibit` on Linux and `caffeinate` on macOS.

```
/plugin install stay-awake@claude_plugins
```

Zero config. Sleep inhibition starts on first tool use, releases when the session ends. See the [plugin README](plugins/stay-awake/README.md) for details.
