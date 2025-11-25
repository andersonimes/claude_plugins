# Contributing to Claude Code Plugin Marketplace

Thank you for your interest in contributing! This guide will help you add your plugin to the marketplace.

## How to Contribute a Plugin

### 1. Choose the Right Category

- **MCP Servers**: Place in `/mcp-servers/your-plugin-name/`
- **Skills**: Place in `/skills/your-skill-name/`
- **Slash Commands**: Place in `/slash-commands/your-command-name/`

### 2. Plugin Structure

Each plugin should be in its own directory with:

```
your-plugin-name/
├── README.md          # Installation and usage instructions
├── <plugin-files>     # Your plugin code
└── package.json       # (if applicable) Dependencies
```

### 3. README Requirements

Your plugin's README should include:

- **Description**: What does your plugin do?
- **Installation**: Step-by-step installation instructions
- **Usage**: Examples of how to use the plugin
- **Configuration**: Any required configuration
- **Requirements**: Dependencies or prerequisites

### 4. Submission Process

1. **Fork** this repository
2. **Create a branch** for your plugin: `git checkout -b add-my-plugin`
3. **Add your plugin** to the appropriate directory
4. **Test** your plugin thoroughly
5. **Commit** your changes: `git commit -m "Add [plugin-name] plugin"`
6. **Push** to your fork: `git push origin add-my-plugin`
7. **Submit a pull request** with a clear description

### 5. Plugin Guidelines

- Code should be well-documented
- Include error handling where appropriate
- Follow Claude Code best practices
- Ensure your plugin doesn't conflict with existing plugins
- Test on multiple platforms if possible

## Questions?

Open an issue if you need help or have questions about contributing!
