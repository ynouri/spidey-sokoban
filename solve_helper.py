#!/usr/bin/env python3
"""Helper script to test level solutions"""

import sys
from test_solutions import SokobanSolver
from levels import LevelManager

def print_level(solver):
    """Print current state of the level"""
    for y, row in enumerate(solver.level_map):
        line = ""
        for x, cell in enumerate(row):
            pos = (x, y)
            if pos == solver.player_pos:
                if pos in solver.targets:
                    line += '+'
                else:
                    line += '@'
            elif pos in solver.boxes:
                if pos in solver.targets:
                    line += '*'
                else:
                    line += '$'
            elif pos in solver.targets:
                line += '.'
            elif pos in solver.walls:
                line += '#'
            else:
                line += ' '
        print(line)
    print()

def test_solution(difficulty, level_num, solution):
    """Test a solution for a level"""
    lm = LevelManager()
    levels = lm.get_levels(difficulty)
    if level_num < 1 or level_num > len(levels):
        print(f"Invalid level number: {level_num}")
        return False

    level_map = levels[level_num - 1]
    solver = SokobanSolver(level_map)

    print(f"\n{difficulty.upper()} LEVEL {level_num}")
    print("=" * 40)
    print("Initial state:")
    print_level(solver)

    print(f"Testing solution: {solution}")
    print(f"Length: {len(solution)} moves\n")

    for i, move in enumerate(solution):
        success = solver.move(move)
        if not success:
            print(f"FAILED at move {i+1}: '{move}'")
            print("Current state:")
            print_level(solver)
            return False

    print("Final state:")
    print_level(solver)

    if solver.is_solved():
        print("✓ SOLVED!")
        return True
    else:
        print("✗ Not solved - boxes not on targets")
        print(f"Boxes: {solver.boxes}")
        print(f"Targets: {solver.targets}")
        return False

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python solve_helper.py <difficulty> <level_num> <solution>")
        print("Example: python solve_helper.py easy 1 RRRUULLDDD")
        sys.exit(1)

    difficulty = sys.argv[1]
    level_num = int(sys.argv[2])
    solution = sys.argv[3]

    test_solution(difficulty, level_num, solution)
