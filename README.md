# Spidey Sokoban

A Sokoban puzzle game for kids featuring Spidey!

## Requirements

- Python 3.x
- pygame
- Pillow (for image processing)
- conda environment named "pygame"

## How to Run

```bash
conda activate pygame
python game.py
```

## How to Play

- **Arrow Keys**: Move Spidey up, down, left, right
- **Goal**: Push all the brown crates onto the green targets
- **R**: Restart the current level
- **N**: Advance to next level (after completing current level)
- **ESC**: Quit the game

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

**Features:**
- 🎨 Comic book themed visuals
- 🎮 5 progressively challenging levels
- 📊 Move counter to track performance
- ⭐ Animated victory celebrations
- 🔄 Easy restart with R key
- ➡️ Level progression with N key

**Next Steps**: Phase 3 - Content
- More levels (target: 10-15 total levels)
- Optional: Sound effects
- Optional: Background music
