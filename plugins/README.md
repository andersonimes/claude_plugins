# Plugins

This directory contains all plugins available in the Claude Code Plugin Marketplace.

## Available Plugins

### [marketplace-help](marketplace-help/)
Get information about the marketplace, available plugins, installation instructions, and contribution guidelines.

**Components**: Commands
**Install**: `/plugin install marketplace-help@plugin_marketplace`

### [session-summarizer](session-summarizer/)
Automatically summarize every Claude Code session into markdown files. Splits multi-topic sessions, includes tags, sample prompts, and links.

**Components**: Hooks (SessionEnd)
**Install**: `/plugin install session-summarizer@plugin_marketplace`
**Config**: Requires `~/.claude/session-summarizer.conf` — see [plugin README](session-summarizer/README.md)

---

## Plugin Structure

Each plugin follows the official Claude Code plugin format:

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json          # Plugin metadata
├── commands/                # Slash commands (optional)
├── agents/                  # Specialized agents (optional)
├── skills/                  # Agent capabilities (optional)
├── hooks/                   # Event handlers (optional)
├── .mcp.json               # MCP server config (optional)
└── README.md               # Documentation
```

## Contributing a Plugin

See [CONTRIBUTING.md](../CONTRIBUTING.md) for detailed instructions on how to add your plugin to the marketplace.

Quick checklist:
- [ ] Create plugin directory in `plugins/`
- [ ] Add `.claude-plugin/plugin.json` with metadata
- [ ] Include your plugin components (commands, agents, etc.)
- [ ] Write comprehensive README.md
- [ ] Test thoroughly
- [ ] Submit pull request

## Installation

To install any plugin from this marketplace:

```bash
# Using Claude Code CLI (recommended)
claude-code plugins install /path/to/plugin_marketplace/plugins/plugin-name

# Or manually
cp -r plugins/plugin-name ~/.claude/plugins/
```

Then restart Claude Code.

## Resources

- [Official Claude Code Plugins](https://github.com/anthropics/claude-code/tree/main/plugins)
- [Marketplace Contribution Guide](../CONTRIBUTING.md)
- [Main Marketplace README](../README.md)
