#!/usr/bin/env python3
"""
Unit tests for Spidey Sokoban levels
Tests that all levels are valid and potentially solvable
"""

import unittest
from pathlib import Path
from levels import LevelManager


class TestLevelValidity(unittest.TestCase):
    """Test that all levels are valid"""

    @classmethod
    def setUpClass(cls):
        """Load all levels once for all tests"""
        cls.level_manager = LevelManager()

    def parse_level(self, level_map):
        """Parse a level and extract game elements

        Returns:
            tuple: (player_count, box_count, target_count, walls, boxes, targets)
        """
        player_count = 0
        box_count = 0
        target_count = 0
        walls = []
        boxes = []
        targets = []

        for y, row in enumerate(level_map):
            for x, cell in enumerate(row):
                pos = (x, y)
                if cell == '#':
                    walls.append(pos)
                elif cell == '@':
                    player_count += 1
                elif cell == '$':
                    box_count += 1
                    boxes.append(pos)
                elif cell == '.':
                    target_count += 1
                    targets.append(pos)
                elif cell == '*':  # Box on target
                    box_count += 1
                    target_count += 1
                    boxes.append(pos)
                    targets.append(pos)
                elif cell == '+':  # Player on target
                    player_count += 1
                    target_count += 1
                    targets.append(pos)

        return player_count, box_count, target_count, walls, boxes, targets

    def test_level_manager_loads_levels(self):
        """Test that level manager loads levels for all difficulties"""
        for difficulty in ['easy', 'medium', 'hard']:
            levels = self.level_manager.get_levels(difficulty)
            self.assertGreater(len(levels), 0,
                             f"No levels loaded for {difficulty} difficulty")

    def test_all_levels_have_one_player(self):
        """Test that each level has exactly one player"""
        for difficulty in ['easy', 'medium', 'hard']:
            levels = self.level_manager.get_levels(difficulty)
            for i, level_map in enumerate(levels):
                player_count, _, _, _, _, _ = self.parse_level(level_map)
                self.assertEqual(player_count, 1,
                               f"{difficulty.capitalize()} level {i+1} has {player_count} players, expected 1")

    def test_all_levels_have_matching_boxes_and_targets(self):
        """Test that each level has equal number of boxes and targets"""
        for difficulty in ['easy', 'medium', 'hard']:
            levels = self.level_manager.get_levels(difficulty)
            for i, level_map in enumerate(levels):
                _, box_count, target_count, _, _, _ = self.parse_level(level_map)
                self.assertEqual(box_count, target_count,
                               f"{difficulty.capitalize()} level {i+1} has {box_count} boxes but {target_count} targets")

    def test_all_levels_have_at_least_one_box(self):
        """Test that each level has at least one box"""
        for difficulty in ['easy', 'medium', 'hard']:
            levels = self.level_manager.get_levels(difficulty)
            for i, level_map in enumerate(levels):
                _, box_count, _, _, _, _ = self.parse_level(level_map)
                self.assertGreater(box_count, 0,
                                 f"{difficulty.capitalize()} level {i+1} has no boxes")

    def test_all_levels_are_rectangular(self):
        """Test that all levels are rectangular (all rows same length)"""
        for difficulty in ['easy', 'medium', 'hard']:
            levels = self.level_manager.get_levels(difficulty)
            for i, level_map in enumerate(levels):
                if len(level_map) == 0:
                    self.fail(f"{difficulty.capitalize()} level {i+1} is empty")
                row_length = len(level_map[0])
                for row_idx, row in enumerate(level_map):
                    self.assertEqual(len(row), row_length,
                                   f"{difficulty.capitalize()} level {i+1} row {row_idx} has length {len(row)}, expected {row_length}")

    def test_all_levels_are_enclosed(self):
        """Test that all levels have walls around the perimeter"""
        for difficulty in ['easy', 'medium', 'hard']:
            levels = self.level_manager.get_levels(difficulty)
            for i, level_map in enumerate(levels):
                # Check top and bottom rows are all walls
                self.assertTrue(all(c == '#' for c in level_map[0]),
                              f"{difficulty.capitalize()} level {i+1} top row is not all walls")
                self.assertTrue(all(c == '#' for c in level_map[-1]),
                              f"{difficulty.capitalize()} level {i+1} bottom row is not all walls")

                # Check left and right columns are all walls
                for row in level_map:
                    self.assertEqual(row[0], '#',
                                   f"{difficulty.capitalize()} level {i+1} left column has non-wall")
                    self.assertEqual(row[-1], '#',
                                   f"{difficulty.capitalize()} level {i+1} right column has non-wall")

    def test_no_boxes_in_unreachable_corners(self):
        """Test that boxes are not placed in corners where they cannot be moved"""
        for difficulty in ['easy', 'medium', 'hard']:
            levels = self.level_manager.get_levels(difficulty)
            for i, level_map in enumerate(levels):
                _, _, _, walls, boxes, targets = self.parse_level(level_map)

                for box_x, box_y in boxes:
                    # Skip if box is already on target (valid end position)
                    if (box_x, box_y) in targets:
                        continue

                    # Check if box is in a corner (walls on two adjacent sides)
                    # Top-left corner
                    if ((box_x - 1, box_y) in walls and (box_x, box_y - 1) in walls):
                        self.fail(f"{difficulty.capitalize()} level {i+1} has box stuck in top-left corner at {(box_x, box_y)}")
                    # Top-right corner
                    if ((box_x + 1, box_y) in walls and (box_x, box_y - 1) in walls):
                        self.fail(f"{difficulty.capitalize()} level {i+1} has box stuck in top-right corner at {(box_x, box_y)}")
                    # Bottom-left corner
                    if ((box_x - 1, box_y) in walls and (box_x, box_y + 1) in walls):
                        self.fail(f"{difficulty.capitalize()} level {i+1} has box stuck in bottom-left corner at {(box_x, box_y)}")
                    # Bottom-right corner
                    if ((box_x + 1, box_y) in walls and (box_x, box_y + 1) in walls):
                        self.fail(f"{difficulty.capitalize()} level {i+1} has box stuck in bottom-right corner at {(box_x, box_y)}")

    def test_level_count_summary(self):
        """Print summary of level counts"""
        print("\n" + "="*50)
        print("LEVEL COUNT SUMMARY")
        print("="*50)
        total = 0
        for difficulty in ['easy', 'medium', 'hard']:
            count = self.level_manager.get_level_count(difficulty)
            total += count
            print(f"{difficulty.capitalize():10s}: {count} levels")
        print(f"{'Total':10s}: {total} levels")
        print("="*50)


if __name__ == '__main__':
    unittest.main(verbosity=2)
