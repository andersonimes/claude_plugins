# Claude Code Plugin Marketplace

A community-driven marketplace for Claude Code plugins following the official Anthropic plugin structure.

## What's Inside

This marketplace contains Claude Code plugins that extend functionality with custom commands, agents, skills, hooks, and MCP servers.

## Plugin Structure

Each plugin in this marketplace follows the official Claude Code plugin format:

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json          # Plugin metadata (name, version, author)
├── commands/                # Slash commands (optional)
├── agents/                  # Specialized agents (optional)
├── skills/                  # Agent capabilities (optional)
├── hooks/                   # Event handlers (optional)
├── .mcp.json               # MCP server config (optional)
└── README.md               # Documentation
```

## Available Plugins

### [marketplace-help](plugins/marketplace-help)
Get information about the marketplace, available plugins, and contribution guidelines.

**Install**: `claude-code plugins install plugins/marketplace-help`

More plugins coming soon! Browse the [plugins/](plugins/) directory or contribute your own.

## Installing Plugins

### Method 1: Claude Code CLI (Recommended)

```bash
claude-code plugins install /path/to/plugin_marketplace/plugins/plugin-name
```

### Method 2: Manual Installation

```bash
cp -r plugins/plugin-name ~/.claude/plugins/
```

Then restart Claude Code.

## Plugin Components

Plugins can include any combination of:

- **Commands** - Custom slash commands (e.g., `/my-command`)
- **Agents** - Specialized AI agents for complex workflows
- **Skills** - Capabilities that agents can utilize
- **Hooks** - Event handlers triggered during development
- **MCP Servers** - External tool integrations

## Contributing

We welcome contributions! To add your plugin:

1. Fork this repository
2. Create your plugin in the `plugins/` directory following the official structure
3. Include a comprehensive README with installation and usage instructions
4. Add plugin metadata in `.claude-plugin/plugin.json`
5. Test your plugin thoroughly
6. Submit a pull request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## Creating a Plugin

### Quick Start

1. Create your plugin directory:
```bash
mkdir -p plugins/my-plugin/.claude-plugin
```

2. Create `plugin.json`:
```json
{
  "name": "my-plugin",
  "description": "What your plugin does",
  "version": "1.0.0",
  "author": {
    "name": "Your Name",
    "email": "your.email@example.com"
  }
}
```

3. Add your components (commands, agents, skills, etc.)

4. Write a README documenting installation and usage

5. Test it: `claude-code plugins install plugins/my-plugin`

## Resources

- [Official Claude Code Plugins](https://github.com/anthropics/claude-code/tree/main/plugins)
- [Claude Code Documentation](https://github.com/anthropics/claude-code)
- [Plugin Development Guide](CONTRIBUTING.md)

## Support

For issues or questions, please open an issue in this repository.

## License

Individual plugins may have their own licenses. Check each plugin's README for details.
