# My Claude Code Plugin Collection

**Private repo** - This is where I store my custom Claude Code plugins following the official Anthropic structure.

## Quick Start: Installing Plugins

### Method 1: Install Directly from GitHub (Easiest!)

Claude Code can consume plugins directly from GitHub without cloning:

**Step 1: Add this repo as a marketplace**

In Claude Code, run:
```
/plugin marketplace add andersonimes/plugin_marketplace
```

**Step 2: Install plugins from the marketplace**

Browse and install interactively:
```
/plugin
```
Then select "Browse Plugins" and choose from your marketplace.

Or install directly by name:
```
/plugin install marketplace-help@plugin_marketplace
```

**Managing plugins:**
```
/plugin enable marketplace-help@plugin_marketplace
/plugin disable marketplace-help@plugin_marketplace
/plugin uninstall marketplace-help@plugin_marketplace
```

### Method 2: Install from Local Clone

If you have this repo cloned locally:

**Add local marketplace:**
```
/plugin marketplace add ~/projects/plugin_marketplace
```

Then install plugins the same way:
```
/plugin install marketplace-help@plugin_marketplace
```

### Method 3: Manual Installation (No Marketplace)

**Copy individual plugin:**
```bash
cp -r ~/projects/plugin_marketplace/plugins/plugin-name ~/.claude/plugins/
```

**Symlink for development:**
```bash
ln -s ~/projects/plugin_marketplace/plugins/plugin-name ~/.claude/plugins/plugin-name
```

**Install all at once:**
```bash
cp -r ~/projects/plugin_marketplace/plugins/* ~/.claude/plugins/
```

Then restart Claude Code.

### Verifying Installation

After installation, restart Claude Code and verify:
- Slash commands: Type `/` to see if your commands appear
- List installed plugins: `/plugin` and select "Manage Installed Plugins"
- Look in `~/.claude/plugins/` to see installed plugins

## Why This Repo Exists

I created this to organize my Claude Code plugins in one place. Initially I set it up with a different structure (organized by type), but then discovered Anthropic has an official plugin format, so I refactored everything to match theirs. This way:

- My plugins follow the community standard
- Each plugin is self-contained and portable
- I can easily share specific plugins later if I want
- The structure matches what I see in the official Anthropic plugins repo
- I can consume plugins directly from GitHub (even though it's private - I'm authenticated)

**Note**: This is a **private repository**. Claude Code can access it because I'm authenticated with GitHub. If I want to share plugins with others, I would either make the repo public or they would need access to this private repo.

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

6. **Commit and push**:
   ```bash
   git add plugins/my-new-plugin
   git commit -m "Add my-new-plugin: brief description"
   git push
   ```

7. **Install from GitHub**:
   ```
   # In Claude Code
   /plugin install my-new-plugin@plugin_marketplace
   ```

   The plugin is automatically available since the marketplace is linked to this GitHub repo!

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
