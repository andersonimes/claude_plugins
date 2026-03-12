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

Requires a config file after install — see the [plugin README](plugins/session-summarizer/README.md) for details.
