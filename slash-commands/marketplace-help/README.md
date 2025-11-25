# Marketplace Help Slash Command

A simple slash command that provides information about the Claude Code Plugin Marketplace.

## Description

This command gives users quick access to information about:
- Available plugins in the marketplace
- How to install and use plugins
- Contributing guidelines
- Plugin categories

## Installation

1. Navigate to your Claude Code commands directory:
   ```bash
   cd ~/.claude/commands/
   ```

2. Copy the command file:
   ```bash
   cp /path/to/plugin_marketplace/slash-commands/marketplace-help/marketplace-info.md ./marketplace-info.md
   ```

3. The command will now be available as `/marketplace-info` in Claude Code

## Usage

In Claude Code, simply type:
```
/marketplace-info
```

You can also ask specific questions:
```
/marketplace-info what MCP servers are available?
/marketplace-info how do I contribute?
```

## Requirements

- Claude Code installed and configured
- No additional dependencies

## Example

```
User: /marketplace-info
Claude: I'll help you explore the Claude Code Plugin Marketplace! This marketplace contains three types of plugins...
```

## Notes

This is a simple example slash command to demonstrate the marketplace structure. Feel free to customize it for your needs!
