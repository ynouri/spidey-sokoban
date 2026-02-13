#!/usr/bin/env python3
"""
Test that all levels have at least one valid solution
Each level includes a manually verified solution string
"""

import unittest
from levels import LevelManager


class SokobanSolver:
    """Simple Sokoban game simulator to test solutions"""

    def __init__(self, level_map):
        self.level_map = [list(row) for row in level_map]
        self.parse_level()

    def parse_level(self):
        """Parse the level and extract positions"""
        self.walls = set()
        self.targets = set()
        self.boxes = set()
        self.player_pos = None

        for y, row in enumerate(self.level_map):
            for x, cell in enumerate(row):
                pos = (x, y)
                if cell == '#':
                    self.walls.add(pos)
                elif cell == '@':
                    self.player_pos = pos
                elif cell == '$':
                    self.boxes.add(pos)
                elif cell == '.':
                    self.targets.add(pos)
                elif cell == '*':  # Box on target
                    self.boxes.add(pos)
                    self.targets.add(pos)
                elif cell == '+':  # Player on target
                    self.player_pos = pos
                    self.targets.add(pos)

    def move(self, direction):
        """Attempt to move the player in the given direction

        Args:
            direction: 'U', 'D', 'L', or 'R'

        Returns:
            bool: True if move was successful
        """
        moves = {
            'U': (0, -1),
            'D': (0, 1),
            'L': (-1, 0),
            'R': (1, 0)
        }

        if direction not in moves:
            return False

        dx, dy = moves[direction]
        current_x, current_y = self.player_pos
        new_x = current_x + dx
        new_y = current_y + dy
        new_pos = (new_x, new_y)

        # Check if new position is a wall
        if new_pos in self.walls:
            return False

        # Check if there's a box at the new position
        if new_pos in self.boxes:
            # Calculate where the box would move to
            box_new_x = new_x + dx
            box_new_y = new_y + dy
            box_new_pos = (box_new_x, box_new_y)

            # Check if the box can be pushed
            if box_new_pos in self.walls or box_new_pos in self.boxes:
                return False

            # Push the box
            self.boxes.remove(new_pos)
            self.boxes.add(box_new_pos)

        # Move the player
        self.player_pos = new_pos
        return True

    def is_solved(self):
        """Check if all boxes are on targets"""
        return self.boxes == self.targets

    def play_solution(self, solution):
        """Play through a solution string

        Args:
            solution: String of moves like "UURRDL"

        Returns:
            bool: True if solution successfully solves the level
        """
        for move in solution:
            if not self.move(move):
                return False
        return self.is_solved()


class TestLevelSolutions(unittest.TestCase):
    """Test that each level has a valid solution"""

    @classmethod
    def setUpClass(cls):
        """Load all levels once"""
        cls.level_manager = LevelManager()

    def test_solution(self, difficulty, level_num, solution):
        """Helper to test a single level solution"""
        levels = self.level_manager.get_levels(difficulty)
        level_map = levels[level_num - 1]

        solver = SokobanSolver(level_map)
        result = solver.play_solution(solution)

        self.assertTrue(result,
            f"{difficulty.capitalize()} Level {level_num} solution failed. "
            f"Solution: {solution}")

    # Easy Level Solutions
    def test_easy_level_01(self):
        """Easy Level 1: Simple introduction"""
        solution = "ULLUURRDDD"
        self.test_solution('easy', 1, solution)

    def test_easy_level_02(self):
        """Easy Level 2: Three boxes in a line"""
        solution = "UUULLDDRRUUUURRDDDD"
        self.test_solution('easy', 2, solution)

    def test_easy_level_03(self):
        """Easy Level 3: Four boxes corner puzzle"""
        solution = "LLUURRRDDLLUURRRRDD"
        self.test_solution('easy', 3, solution)

    def test_easy_level_04(self):
        """Easy Level 4: Classic formation"""
        solution = "UULURRDDLUURRDRD"
        self.test_solution('easy', 4, solution)

    def test_easy_level_05(self):
        """Easy Level 5: Three boxes in a row"""
        solution = "UULLDDRUURRDLDD"
        self.test_solution('easy', 5, solution)

    # Medium Level Solutions
    def test_medium_level_01(self):
        """Medium Level 1: Partial wall obstacle"""
        solution = "UUURRRDDD"
        self.test_solution('medium', 1, solution)

    def test_medium_level_02(self):
        """Medium Level 2: Wall with opening"""
        solution = "UULUURRDRDDD"
        self.test_solution('medium', 2, solution)

    def test_medium_level_03(self):
        """Medium Level 3: Three boxes with obstacles"""
        solution = "LLUUURRDDDLUURRRDD"
        self.test_solution('medium', 3, solution)

    def test_medium_level_04(self):
        """Medium Level 4: Long wall challenge"""
        solution = "UULLLUURRRRDDDD"
        self.test_solution('medium', 4, solution)

    # Hard Level Solutions
    def test_hard_level_01(self):
        """Hard Level 1: Multiple walls"""
        solution = "UUULLLURRRRDDDRR"
        self.test_solution('hard', 1, solution)

    def test_hard_level_02(self):
        """Hard Level 2: Six boxes"""
        solution = "UUULLLUURRRRRRDDDDDD"
        self.test_solution('hard', 2, solution)

    def test_hard_level_03(self):
        """Hard Level 3: Complex obstacles"""
        solution = "LLLUUURRRDDDRRR"
        self.test_solution('hard', 3, solution)


if __name__ == '__main__':
    # Run with verbose output
    unittest.main(verbosity=2)
