# Marketplace Help Plugin

A Claude Code plugin that provides information about the Plugin Marketplace.

## Description

This plugin gives users quick access to information about:
- Available plugins in the marketplace
- How to install and use plugins
- Contributing guidelines
- Plugin categories and structure

## Components

- **Commands**: `/marketplace-info` - Get information about the marketplace

## Installation

### Option 1: Install via Claude Code CLI (recommended)

```bash
claude-code plugins install /path/to/plugin_marketplace/plugins/marketplace-help
```

### Option 2: Manual Installation

1. Copy the plugin directory to your Claude Code plugins directory:
   ```bash
   cp -r plugins/marketplace-help ~/.claude/plugins/
   ```

2. Restart Claude Code

## Usage

Once installed, you can use the following command:

```
/marketplace-info
```

You can also ask specific questions:
```
/marketplace-info what plugins are available?
/marketplace-info how do I contribute?
```

## Plugin Structure

```
marketplace-help/
├── .claude-plugin/
│   └── plugin.json              # Plugin metadata
├── commands/
│   └── marketplace-info.md      # The slash command
└── README.md                    # This file
```

## Requirements

- Claude Code installed and configured
- No additional dependencies

## Version History

- **1.0.0** - Initial release with marketplace-info command

## Contributing

Found a bug or want to improve this plugin? Submit a pull request to the marketplace repository!

## License

This plugin is part of the Claude Code Plugin Marketplace.
