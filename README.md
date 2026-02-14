# Spidey Sokoban

A Sokoban puzzle game for kids featuring Spidey!

## Quick Start (Recommended)

**One-liner to clone and run (assuming `uv` is installed):**

```bash
git clone https://github.com/yourusername/spidey-sokoban.git && cd spidey-sokoban && uv run --no-project game.py
```

**First-time setup (if you don't have `uv`):**

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Then run the one-liner above
```

That's it! `uv` automatically handles everything - no manual setup needed! 🎮

## Alternative Installation Methods

### Using Python + pip

```bash
# Clone the repository
git clone https://github.com/yourusername/spidey-sokoban.git
cd spidey-sokoban

# Install dependencies
pip install pygame pillow

# Run the game
python game.py
```

### Using conda

```bash
# Clone the repository
git clone https://github.com/yourusername/spidey-sokoban.git
cd spidey-sokoban

# Create and activate environment
conda create -n pygame python=3.11
conda activate pygame

# Install dependencies
pip install pygame pillow

# Run the game
python game.py
```

## Requirements

- Python 3.9+
- pygame 2.5.0+
- Pillow 10.0.0+

## How to Play

**Mode Selection:**
- **UP/DOWN**: Select mode (Custom Levels or Original Sokoban)
- **ENTER or SPACE**: Confirm selection
- **ESC**: Quit game

**Difficulty Selection (Custom mode only):**
- **UP/DOWN**: Select difficulty (Easy/Medium/Hard)
- **ENTER or SPACE**: Start game
- **ESC**: Return to mode selection

**In Game:**
- **Arrow Keys**: Move Spin up, down, left, right
- **Goal**: Push all the brown crates onto the green targets
- **R**: Restart the current level
- **N**: Advance to next level (after completing current level)
- **ESC**: Return to main menu

## Game Elements

- 🕷️ **Spin (Miles Morales)**: Cute chibi-style Spider-Man sprite (the player)
- 📦 **Crates**: Brown wooden boxes with plank lines to push
- 🎯 **Targets**: Glowing green circles with highlights
- 🧱 **Walls**: Comic-style panels with thick black borders
- ⬜ **Floor**: White tiles with gray borders
- ✨ **Visual Effects**: Boxes glow green when on targets, victory stars animation

## Current Status

**Phase 1 Complete ✅**: Core Game
- ✅ Basic window and game loop
- ✅ Grid-based level display
- ✅ Player movement with arrow keys
- ✅ Box pushing mechanics
- ✅ Win condition detection

**Phase 2 Complete ✅**: Polish & Features
- ✅ Spidey-themed graphics with comic book style
- ✅ 5 levels with varying difficulty
- ✅ Level progression system
- ✅ Visual polish (gradient background, title, shadows)
- ✅ Move counter
- ✅ Victory animation with pulsing stars
- ✅ Level indicator

**Iteration B Complete ✅**: Spidey Sprites
- ✅ Larger window (1200x800) and tiles (80px)
- ✅ Actual Spin character sprite with transparent background
- ✅ Image processing to remove white background
- ✅ Proper sprite scaling and centering

**Iteration C Complete ✅**: More Levels & Testing
- ✅ 12 total levels across 3 difficulty levels
- ✅ Difficulty selection menu (Easy/Medium/Hard)
- ✅ Level file system (levels organized by difficulty)
- ✅ Internal walls/obstacles in medium and hard levels
- ✅ LevelManager class for level loading
- ✅ Comprehensive unit tests for level validation
- ✅ All levels verified to be valid and properly formatted

**Iteration E Complete ✅**: Original Sokoban Levels
- ✅ Added 90 original Sokoban levels from classic collection
- ✅ Mode selection menu (Custom vs Original)
- ✅ Updated menu flow with multiple screens
- ✅ Level parser for original format
- ✅ Total: 102 levels (12 custom + 90 original)

**Features:**
- 🎨 Comic book themed visuals
- 🎮 **102 total levels!**
  - **Custom Levels (12):**
    - Easy: 5 levels
    - Medium: 4 levels (with internal obstacles)
    - Hard: 3 levels (complex puzzles)
  - **Original Sokoban (90):**
    - Classic collection from original game
    - Progressive difficulty
- 🎯 Two game modes: Custom or Original
- 📊 Move counter to track performance
- ⭐ Animated victory celebrations
- 🔄 Easy restart with R key
- ➡️ Level progression with N key
- 📂 Level file system for easy expansion
- ✅ Unit tested for level validity

**Potential Future Enhancements:**
- More levels (currently 12, could expand to 20+)
- Additional character sprites (Spidey, Ghost-Spider)
- Sound effects (box push, level complete, etc.)
- Background music
- Level editor
- Save/load progress
- Time tracking and best times
