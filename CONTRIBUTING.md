# Contributing to Claude Code Plugin Marketplace

Thank you for your interest in contributing! This guide will help you add your plugin to the marketplace.

## Plugin Structure

All plugins must follow the official Claude Code plugin structure:

```
plugins/your-plugin-name/
├── .claude-plugin/
│   └── plugin.json          # Required: Plugin metadata
├── commands/                # Optional: Slash commands
├── agents/                  # Optional: Specialized agents
├── skills/                  # Optional: Agent capabilities
├── hooks/                   # Optional: Event handlers
├── .mcp.json               # Optional: MCP server config
└── README.md               # Required: Documentation
```

## Step-by-Step Guide

### 1. Fork the Repository

Click the "Fork" button on GitHub to create your own copy of the marketplace.

### 2. Create Your Plugin Directory

```bash
cd plugins
mkdir -p your-plugin-name/.claude-plugin
cd your-plugin-name
```

### 3. Create plugin.json (Required)

Create `.claude-plugin/plugin.json` with your plugin metadata:

```json
{
  "name": "your-plugin-name",
  "description": "A clear description of what your plugin does",
  "version": "1.0.0",
  "author": {
    "name": "Your Name",
    "email": "your.email@example.com"
  }
}
```

**Fields:**
- `name` (required): Plugin identifier, should match directory name
- `description` (required): What your plugin does
- `version` (required): Semantic version (e.g., "1.0.0")
- `author` (required): Your name and email

### 4. Add Plugin Components

Depending on what your plugin provides, create the appropriate directories:

#### Commands (`commands/`)

Slash commands are markdown files that provide instructions to Claude:

```bash
mkdir commands
```

Create `commands/my-command.md`:
```markdown
You are helping the user with [specific task].

Follow these steps:
1. [Step one]
2. [Step two]
...
```

The filename becomes the command name (e.g., `/my-command`).

#### Agents (`agents/`)

Specialized agents for complex workflows. See [official examples](https://github.com/anthropics/claude-code/tree/main/plugins) for structure.

#### Skills (`skills/`)

Reusable capabilities that agents can utilize. See official documentation.

#### Hooks (`hooks/`)

Event handlers triggered during development workflows.

#### MCP Servers (`.mcp.json`)

For external tool integrations, create `.mcp.json`:
```json
{
  "mcpServers": {
    "your-server": {
      "command": "node",
      "args": ["path/to/server.js"]
    }
  }
}
```

### 5. Write Documentation (Required)

Create a comprehensive `README.md` that includes:

```markdown
# Your Plugin Name

Brief description of what your plugin does.

## Description

Detailed explanation of functionality and use cases.

## Components

List what's included (commands, agents, skills, etc.)

## Installation

### Option 1: Claude Code CLI
\`\`\`bash
claude-code plugins install /path/to/plugin_marketplace/plugins/your-plugin-name
\`\`\`

### Option 2: Manual Installation
\`\`\`bash
cp -r plugins/your-plugin-name ~/.claude/plugins/
\`\`\`

## Usage

Provide examples of how to use your plugin.

## Requirements

List any dependencies or prerequisites.

## Version History

- **1.0.0** - Initial release

## License

Specify your license.
```

### 6. Test Your Plugin

Before submitting, test thoroughly:

```bash
# Install locally
claude-code plugins install /path/to/your-plugin

# Test all commands/features
# Verify it works as expected
# Check for conflicts with other plugins
```

### 7. Update Marketplace README

Add your plugin to the "Available Plugins" section in the main `README.md`:

```markdown
### [your-plugin-name](plugins/your-plugin-name)
Brief description of what it does.

**Install**: `claude-code plugins install plugins/your-plugin-name`
```

### 8. Submit Pull Request

```bash
# Add your changes
git add plugins/your-plugin-name
git add README.md

# Commit with descriptive message
git commit -m "Add [your-plugin-name] plugin: [brief description]"

# Push to your fork
git push origin main

# Create pull request on GitHub
```

## Plugin Guidelines

### Code Quality
- Follow JavaScript/TypeScript best practices
- Include error handling
- Add comments for complex logic
- Use meaningful variable names

### Documentation
- Clear installation instructions
- Usage examples for all features
- List all requirements and dependencies
- Include troubleshooting tips

### Testing
- Test on multiple platforms if possible (macOS, Linux, Windows)
- Verify no conflicts with existing plugins
- Ensure all commands/features work as documented

### Compatibility
- Specify Claude Code version requirements if any
- Note any platform-specific limitations
- List all external dependencies

### Security
- Never include API keys or secrets
- Validate user input
- Follow security best practices
- Warn users about any elevated permissions needed

## Pull Request Template

When submitting your PR, include:

```
## Plugin: [Your Plugin Name]

**Description**: [What does it do?]

**Components**:
- [ ] Commands
- [ ] Agents
- [ ] Skills
- [ ] Hooks
- [ ] MCP Server

**Testing**:
- [ ] Tested on [OS]
- [ ] No conflicts with existing plugins
- [ ] All features work as documented

**Documentation**:
- [ ] README.md included
- [ ] Usage examples provided
- [ ] Installation instructions clear

**Additional Notes**:
[Any other relevant information]
```

## Getting Help

- Review [official Claude Code plugins](https://github.com/anthropics/claude-code/tree/main/plugins) for examples
- Check existing marketplace plugins for reference
- Open an issue if you have questions
- Join discussions for plugin development tips

## Code of Conduct

- Be respectful and constructive
- Help others learn and improve
- Focus on making great plugins
- Collaborate and share knowledge

Thank you for contributing to the Claude Code Plugin Marketplace!
