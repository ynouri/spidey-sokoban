#!/usr/bin/env python3
"""
Spidey Sokoban - A Sokoban game for kids featuring Spidey!
"""

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60
TILE_SIZE = 60  # Large tiles for young players

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (41, 128, 185)
GRAY = (169, 169, 169)
DARK_GRAY = (64, 64, 64)
LIGHT_BLUE = (173, 216, 230)
RED = (231, 76, 60)
ORANGE = (230, 126, 34)
GREEN = (46, 204, 113)
YELLOW = (241, 196, 15)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Spidey Sokoban")
        self.clock = pygame.time.Clock()
        self.running = True

        # Level 1: Simple level with 2 boxes
        # '#' = wall, ' ' = floor, '@' = player, '$' = box, '.' = target
        self.level_map = [
            "########",
            "#      #",
            "# .$   #",
            "# $@ . #",
            "#      #",
            "########"
        ]

        self.load_level()
        self.level_complete = False

    def load_level(self):
        """Parse the level map and initialize game state"""
        self.walls = []
        self.targets = []
        self.boxes = []
        self.player_pos = None

        for y, row in enumerate(self.level_map):
            for x, cell in enumerate(row):
                pos = (x, y)
                if cell == '#':
                    self.walls.append(pos)
                elif cell == '@':
                    self.player_pos = pos
                elif cell == '$':
                    self.boxes.append(pos)
                elif cell == '.':
                    self.targets.append(pos)
                elif cell == '*':  # Box on target
                    self.boxes.append(pos)
                    self.targets.append(pos)
                elif cell == '+':  # Player on target
                    self.player_pos = pos
                    self.targets.append(pos)

        # Calculate offset to center the level
        level_width = len(self.level_map[0]) * TILE_SIZE
        level_height = len(self.level_map) * TILE_SIZE
        self.offset_x = (WINDOW_WIDTH - level_width) // 2
        self.offset_y = (WINDOW_HEIGHT - level_height) // 2

    def move_player(self, dx, dy):
        """Try to move the player in the given direction"""
        if not self.player_pos:
            return

        current_x, current_y = self.player_pos
        new_x = current_x + dx
        new_y = current_y + dy
        new_pos = (new_x, new_y)

        # Check if new position is a wall
        if new_pos in self.walls:
            return

        # Check if there's a box at the new position
        if new_pos in self.boxes:
            # Calculate where the box would move to
            box_new_x = new_x + dx
            box_new_y = new_y + dy
            box_new_pos = (box_new_x, box_new_y)

            # Check if the box can be pushed
            if box_new_pos in self.walls or box_new_pos in self.boxes:
                return  # Can't push box into wall or another box

            # Push the box
            self.boxes.remove(new_pos)
            self.boxes.append(box_new_pos)

        # Move the player
        self.player_pos = new_pos

        # Check if level is complete
        self.check_win()

    def check_win(self):
        """Check if all boxes are on targets"""
        for box in self.boxes:
            if box not in self.targets:
                return  # At least one box is not on a target

        # All boxes are on targets!
        self.level_complete = True

    def handle_events(self):
        """Handle input events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_r:
                    # Restart level
                    self.level_complete = False
                    self.load_level()
                elif not self.level_complete:
                    # Only allow movement if level not complete
                    if event.key == pygame.K_UP:
                        self.move_player(0, -1)
                    elif event.key == pygame.K_DOWN:
                        self.move_player(0, 1)
                    elif event.key == pygame.K_LEFT:
                        self.move_player(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.move_player(1, 0)

    def update(self):
        """Update game state"""
        pass

    def draw(self):
        """Draw everything to the screen"""
        self.screen.fill(LIGHT_BLUE)

        # Draw floor (for all non-wall positions)
        for y, row in enumerate(self.level_map):
            for x, cell in enumerate(row):
                if cell != '#':
                    rect = pygame.Rect(
                        self.offset_x + x * TILE_SIZE,
                        self.offset_y + y * TILE_SIZE,
                        TILE_SIZE,
                        TILE_SIZE
                    )
                    pygame.draw.rect(self.screen, WHITE, rect)
                    pygame.draw.rect(self.screen, GRAY, rect, 2)

        # Draw walls
        for x, y in self.walls:
            rect = pygame.Rect(
                self.offset_x + x * TILE_SIZE,
                self.offset_y + y * TILE_SIZE,
                TILE_SIZE,
                TILE_SIZE
            )
            pygame.draw.rect(self.screen, DARK_GRAY, rect)
            pygame.draw.rect(self.screen, BLACK, rect, 3)

        # Draw targets (green circles)
        for x, y in self.targets:
            center_x = self.offset_x + x * TILE_SIZE + TILE_SIZE // 2
            center_y = self.offset_y + y * TILE_SIZE + TILE_SIZE // 2
            pygame.draw.circle(self.screen, GREEN, (center_x, center_y), TILE_SIZE // 3)
            pygame.draw.circle(self.screen, DARK_GRAY, (center_x, center_y), TILE_SIZE // 3, 3)

        # Draw boxes (orange squares)
        for x, y in self.boxes:
            rect = pygame.Rect(
                self.offset_x + x * TILE_SIZE + 8,
                self.offset_y + y * TILE_SIZE + 8,
                TILE_SIZE - 16,
                TILE_SIZE - 16
            )
            pygame.draw.rect(self.screen, ORANGE, rect)
            pygame.draw.rect(self.screen, DARK_GRAY, rect, 3)

        # Draw player (red circle for Spidey)
        if self.player_pos:
            x, y = self.player_pos
            center_x = self.offset_x + x * TILE_SIZE + TILE_SIZE // 2
            center_y = self.offset_y + y * TILE_SIZE + TILE_SIZE // 2
            pygame.draw.circle(self.screen, RED, (center_x, center_y), TILE_SIZE // 2 - 5)
            pygame.draw.circle(self.screen, BLACK, (center_x, center_y), TILE_SIZE // 2 - 5, 3)

        # Draw victory message if level complete
        if self.level_complete:
            # Semi-transparent overlay
            overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
            overlay.set_alpha(200)
            overlay.fill(BLACK)
            self.screen.blit(overlay, (0, 0))

            # Victory text
            font_large = pygame.font.Font(None, 80)
            font_small = pygame.font.Font(None, 40)

            victory_text = font_large.render("LEVEL COMPLETE!", True, YELLOW)
            victory_rect = victory_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 40))
            self.screen.blit(victory_text, victory_rect)

            restart_text = font_small.render("Press R to restart", True, WHITE)
            restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 40))
            self.screen.blit(restart_text, restart_rect)

        pygame.display.flip()

    def run(self):
        """Main game loop"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
