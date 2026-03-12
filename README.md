# Claude Code Plugin Marketplace

A collection of plugins for [Claude Code](https://docs.anthropic.com/en/docs/claude-code).

## Setup

Add this marketplace to Claude Code:

```
/plugin marketplace add andersonimes/plugin_marketplace
```

Then install plugins by name:

```
/plugin install <plugin-name>@plugin_marketplace
```

## Plugins

### [session-summarizer](plugins/session-summarizer/)

Automatically summarizes every Claude Code session into markdown files when the conversation ends. Splits multi-topic sessions, includes tags, sample prompts, and relevant links.

```
/plugin install session-summarizer@plugin_marketplace
```

Requires a config file after install — see the [plugin README](plugins/session-summarizer/README.md) for details.
