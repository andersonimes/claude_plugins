# My Claude Code Plugin Collection

**Private repo** - This is where I store my custom Claude Code plugins following the official Anthropic structure.

## Quick Start: Installing Plugins

### Installing Individual Plugins

To use a plugin from this marketplace:

**Option 1 - Claude Code CLI (Recommended):**
```bash
claude-code plugins install ~/projects/plugin_marketplace/plugins/plugin-name
```

**Option 2 - Manual Installation:**
```bash
# Copy plugin to Claude Code plugins directory
cp -r ~/projects/plugin_marketplace/plugins/plugin-name ~/.claude/plugins/

# Restart Claude Code
```

**Option 3 - Symlink (for development):**
```bash
# Create symlink so changes sync automatically
ln -s ~/projects/plugin_marketplace/plugins/plugin-name ~/.claude/plugins/plugin-name
```

### Installing All Plugins at Once

To install every plugin from this marketplace:

```bash
# Install all at once
for plugin in ~/projects/plugin_marketplace/plugins/*/; do
  claude-code plugins install "$plugin"
done
```

Or manually:
```bash
cp -r ~/projects/plugin_marketplace/plugins/* ~/.claude/plugins/
```

### Verifying Installation

After installation, restart Claude Code and verify:
- Slash commands: Type `/` to see if your commands appear
- Check installed plugins: `claude-code plugins list` (if supported)
- Look in `~/.claude/plugins/` to see installed plugins

## Why This Repo Exists

I created this to organize my Claude Code plugins in one place. Initially I set it up with a different structure (organized by type), but then discovered Anthropic has an official plugin format, so I refactored everything to match theirs. This way:

- My plugins follow the community standard
- Each plugin is self-contained and portable
- I can easily share specific plugins later if I want
- The structure matches what I see in the official Anthropic plugins repo

## How Plugin Structure Works

Each plugin lives in `plugins/plugin-name/` and follows this format:

```
plugins/my-plugin/
├── .claude-plugin/
│   └── plugin.json          # Metadata: name, description, version, author
├── commands/                # Slash commands (optional)
├── agents/                  # Specialized agents (optional)
├── skills/                  # Agent capabilities (optional)
├── hooks/                   # Event handlers (optional)
├── .mcp.json               # MCP server config (optional)
└── README.md               # What it does and how to use it
```

**Key insight**: Plugins aren't organized by type anymore. Each plugin is a complete package that can contain multiple types of things (commands, agents, skills, etc.).

## My Plugins

### marketplace-help
A simple command that provides info about this marketplace. Created it as my first example plugin.

**Components**: Commands (`/marketplace-info`)
**Install**: `claude-code plugins install ~/projects/plugin_marketplace/plugins/marketplace-help`

## How to Create a New Plugin

When I want to add a new plugin:

1. **Create the directory structure:**
   ```bash
   cd ~/projects/plugin_marketplace/plugins
   mkdir -p my-new-plugin/.claude-plugin
   cd my-new-plugin
   ```

2. **Create `plugin.json`:**
   ```bash
   cat > .claude-plugin/plugin.json << 'EOF'
   {
     "name": "my-new-plugin",
     "description": "What this plugin does",
     "version": "1.0.0",
     "author": {
       "name": "Anderson Imes",
       "email": "your-email@example.com"
     }
   }
   EOF
   ```

3. **Add components I need:**
   - `mkdir commands` for slash commands
   - `mkdir agents` for custom agents
   - `mkdir skills` for reusable skills
   - `mkdir hooks` for event handlers
   - Create `.mcp.json` for MCP server integrations

4. **Write a README** so I remember what it does

5. **Test it**: `claude-code plugins install ~/projects/plugin_marketplace/plugins/my-new-plugin`

6. **Commit it**:
   ```bash
   git add plugins/my-new-plugin
   git commit -m "Add my-new-plugin: brief description"
   git push
   ```

## Quick Reference: Plugin Components

- **Commands** (`commands/*.md`) - Slash commands. Filename = command name. Just markdown files with instructions.
- **Agents** (`agents/`) - Specialized AI agents for complex multi-step tasks
- **Skills** (`skills/`) - Reusable capabilities that agents can invoke
- **Hooks** (`hooks/`) - Code that runs on events (before/after tool calls, etc.)
- **MCP Servers** (`.mcp.json`) - External tool integrations (APIs, databases, etc.)

## Repo History

- First commit: Created with type-based organization (mcp-servers/, skills/, slash-commands/)
- Second commit: Refactored to official Anthropic plugin structure after discovering their format

## Resources for Future Me

- [Official Anthropic Plugins](https://github.com/anthropics/claude-code/tree/main/plugins) - Good examples to reference
- [CONTRIBUTING.md](CONTRIBUTING.md) - Detailed guide I wrote for myself on plugin structure
- [plugins/README.md](plugins/README.md) - Quick overview of what's in the plugins directory

## Repository Info

- **Local path**: `~/projects/plugin_marketplace/`
- **GitHub**: https://github.com/andersonimes/plugin_marketplace (private)
- **Clone command**: `git clone https://github.com/andersonimes/plugin_marketplace.git`

## Git Commands I'll Need

```bash
# See what changed
git status

# Add new plugin
git add plugins/my-plugin
git commit -m "Add my-plugin: description"

# Push to GitHub
git push

# Pull latest (if I make changes from another machine)
git pull
```
