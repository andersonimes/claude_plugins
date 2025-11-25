# Slash Commands

Custom slash commands for quick actions and workflows in Claude Code.

## What are Slash Commands?

Slash commands provide quick access to:
- Common tasks and workflows
- Custom prompts
- Templated responses
- Project-specific actions

## Available Commands

- **marketplace-help** - Get information about this marketplace

More coming soon! Be the first to contribute.

## Contributing

To add your slash command:

1. Create a directory with your command name
2. Add a `.md` file with the command prompt/instructions
3. Include a README with:
   - Description
   - Installation instructions
   - Usage examples
4. Submit a pull request

See [CONTRIBUTING.md](../CONTRIBUTING.md) for detailed guidelines.

## Installing Slash Commands

To install a command from this marketplace:

1. Navigate to the command's directory
2. Copy the `.md` file to `~/.claude/commands/`
3. The command will be available as `/command-name` in Claude Code

## Creating Commands

Slash commands are markdown files containing instructions for Claude. The file name becomes the command name.

Example structure:
```markdown
You are helping the user with [specific task].

Follow these steps:
1. [Step one]
2. [Step two]
...
```

## Resources

- [Claude Code Commands Documentation](https://github.com/anthropics/claude-code)
