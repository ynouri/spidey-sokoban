#!/usr/bin/env python3
"""
Level management system for Spidey Sokoban
Handles loading levels from files organized by difficulty
"""

import os
from pathlib import Path


class LevelManager:
    """Manages level loading and organization"""

    DIFFICULTIES = ['easy', 'medium', 'hard']

    def __init__(self, levels_dir='levels'):
        """Initialize the level manager

        Args:
            levels_dir: Path to the levels directory
        """
        self.levels_dir = Path(levels_dir)
        self.levels_cache = {}
        self._load_all_levels()

    def _load_all_levels(self):
        """Load all levels from files into cache"""
        for difficulty in self.DIFFICULTIES:
            self.levels_cache[difficulty] = []
            difficulty_path = self.levels_dir / difficulty

            if not difficulty_path.exists():
                print(f"Warning: {difficulty_path} does not exist")
                continue

            # Get all .txt files and sort them
            level_files = sorted(difficulty_path.glob('level_*.txt'))

            for level_file in level_files:
                try:
                    level_data = self._load_level_file(level_file)
                    self.levels_cache[difficulty].append(level_data)
                except Exception as e:
                    print(f"Error loading {level_file}: {e}")

    def _load_level_file(self, filepath):
        """Load a single level file

        Args:
            filepath: Path to the level file

        Returns:
            List of strings representing the level map
        """
        with open(filepath, 'r') as f:
            lines = f.read().strip().split('\n')
        return lines

    def get_levels(self, difficulty):
        """Get all levels for a specific difficulty

        Args:
            difficulty: 'easy', 'medium', or 'hard'

        Returns:
            List of level maps
        """
        if difficulty not in self.DIFFICULTIES:
            raise ValueError(f"Invalid difficulty: {difficulty}")
        return self.levels_cache.get(difficulty, [])

    def get_level_count(self, difficulty):
        """Get the number of levels for a difficulty

        Args:
            difficulty: 'easy', 'medium', or 'hard'

        Returns:
            Number of levels
        """
        return len(self.get_levels(difficulty))

    def get_total_levels(self):
        """Get total number of levels across all difficulties

        Returns:
            Total count of levels
        """
        return sum(len(levels) for levels in self.levels_cache.values())
