# Installation Guide

## For Players (Easiest Method)

### macOS

1. **Install uv** (one-time setup):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Download and run the game**:
   ```bash
   git clone https://github.com/yourusername/spidey-sokoban.git
   cd spidey-sokoban
   uv run game.py
   ```

That's it! The first run will take a moment to set up the environment, but subsequent runs will be instant.

### Why uv?

- **Zero manual setup**: No need to manage Python versions or virtual environments
- **Automatic dependencies**: Installs pygame and Pillow automatically
- **Fast**: Written in Rust, extremely quick
- **Isolated**: Doesn't interfere with your system Python

## Alternative Methods

See [README.md](README.md) for installation using pip or conda.

## Troubleshooting

### "command not found: uv"

After installing uv, you may need to restart your terminal or run:
```bash
source ~/.zshrc  # or ~/.bashrc
```

### "git: command not found"

Install git first:
```bash
# macOS
brew install git

# Or download from: https://git-scm.com/downloads
```

### Game window doesn't appear

Make sure you have display access. On macOS, you might need to:
1. Grant terminal/iTerm2 screen recording permissions in System Preferences
2. Try running from a different terminal

## For Developers

If you want to contribute or run tests:

```bash
# Clone and enter directory
git clone https://github.com/yourusername/spidey-sokoban.git
cd spidey-sokoban

# Run the game
uv run game.py

# Run tests
uv run python test_levels.py

# Run with Python directly (after uv sync)
uv sync
uv run python game.py
```
