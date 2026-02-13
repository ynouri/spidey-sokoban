#!/usr/bin/env python3
"""
Spidey Sokoban - A Sokoban game for kids featuring Spidey!
"""

import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60
TILE_SIZE = 60  # Large tiles for young players

# Colors - Comic Book Theme
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (41, 128, 185)
GRAY = (169, 169, 169)
DARK_GRAY = (64, 64, 64)
LIGHT_BLUE = (173, 216, 230)
SPIDEY_RED = (220, 20, 60)  # Crimson for Spidey
SPIDEY_BLUE = (0, 71, 171)  # Deep blue for Spidey
WEB_GRAY = (200, 200, 200)  # Light gray for webs
ORANGE = (230, 126, 34)
BROWN = (139, 69, 19)
GREEN = (46, 204, 113)
LIME = (50, 205, 50)
YELLOW = (241, 196, 15)
PURPLE = (142, 68, 173)  # For comic style

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Spidey Sokoban")
        self.clock = pygame.time.Clock()
        self.running = True

        # Collection of levels
        # '#' = wall, ' ' = floor, '@' = player, '$' = box, '.' = target
        self.levels = [
            # Level 1: Simple introduction
            [
                "########",
                "#      #",
                "# .$   #",
                "# $@ . #",
                "#      #",
                "########"
            ],
            # Level 2: Three boxes in a line
            [
                "#########",
                "#   .   #",
                "#   $   #",
                "#   $   #",
                "#   $   #",
                "#   @   #",
                "#   .   #",
                "#   .   #",
                "#########"
            ],
            # Level 3: Corner puzzle
            [
                "##########",
                "#        #",
                "# $$     #",
                "#  @     #",
                "#        #",
                "#     .. #",
                "#     .. #",
                "##########"
            ],
            # Level 4: Classic formation
            [
                "#######",
                "#     #",
                "# .$. #",
                "# $.$ #",
                "#  @  #",
                "#     #",
                "#######"
            ],
            # Level 5: Challenge
            [
                "##########",
                "#        #",
                "# $ $ $  #",
                "#   @    #",
                "#        #",
                "#  . . . #",
                "##########"
            ]
        ]

        self.current_level = 0
        self.load_level()
        self.level_complete = False
        self.move_count = 0
        self.victory_frame = 0  # For victory animation

    def load_level(self):
        """Parse the level map and initialize game state"""
        self.level_map = self.levels[self.current_level]
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

        # Reset move counter and victory animation
        self.move_count = 0
        self.victory_frame = 0

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
        self.move_count += 1

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
                elif event.key == pygame.K_n and self.level_complete:
                    # Next level
                    if self.current_level < len(self.levels) - 1:
                        self.current_level += 1
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
        if self.level_complete:
            self.victory_frame += 1

    def draw(self):
        """Draw everything to the screen"""
        # Gradient background (darker at bottom)
        for y in range(WINDOW_HEIGHT):
            color_value = int(173 + (y / WINDOW_HEIGHT) * 40)
            color = (color_value, 216, 230)
            pygame.draw.line(self.screen, color, (0, y), (WINDOW_WIDTH, y))

        # Draw title
        font_title = pygame.font.Font(None, 56)
        title = font_title.render("SPIDEY SOKOBAN", True, SPIDEY_RED)
        title_shadow = font_title.render("SPIDEY SOKOBAN", True, BLACK)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, 30))
        shadow_rect = title_rect.copy()
        shadow_rect.x += 3
        shadow_rect.y += 3
        self.screen.blit(title_shadow, shadow_rect)
        self.screen.blit(title, title_rect)

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

        # Draw walls (comic book panel style)
        for x, y in self.walls:
            rect = pygame.Rect(
                self.offset_x + x * TILE_SIZE,
                self.offset_y + y * TILE_SIZE,
                TILE_SIZE,
                TILE_SIZE
            )
            # Gradient effect - darker at bottom
            pygame.draw.rect(self.screen, (80, 80, 90), rect)
            pygame.draw.rect(self.screen, BLACK, rect, 5)  # Thick comic border
            # Add inner highlight
            inner_rect = pygame.Rect(rect.x + 5, rect.y + 5, rect.width - 10, rect.height - 10)
            pygame.draw.rect(self.screen, (100, 100, 110), inner_rect, 2)

        # Draw targets (glowing green circles)
        for x, y in self.targets:
            center_x = self.offset_x + x * TILE_SIZE + TILE_SIZE // 2
            center_y = self.offset_y + y * TILE_SIZE + TILE_SIZE // 2
            # Outer glow
            pygame.draw.circle(self.screen, LIME, (center_x, center_y), TILE_SIZE // 3 + 2)
            # Main circle
            pygame.draw.circle(self.screen, GREEN, (center_x, center_y), TILE_SIZE // 3)
            # Inner highlight
            pygame.draw.circle(self.screen, LIME, (center_x - 5, center_y - 5), TILE_SIZE // 6)
            # Border
            pygame.draw.circle(self.screen, BLACK, (center_x, center_y), TILE_SIZE // 3, 3)

        # Draw boxes (crate style with wood texture)
        for x, y in self.boxes:
            rect = pygame.Rect(
                self.offset_x + x * TILE_SIZE + 8,
                self.offset_y + y * TILE_SIZE + 8,
                TILE_SIZE - 16,
                TILE_SIZE - 16
            )
            # Main box color
            pygame.draw.rect(self.screen, BROWN, rect)
            # Add wood plank lines
            pygame.draw.line(self.screen, BLACK,
                           (rect.left, rect.centery), (rect.right, rect.centery), 2)
            pygame.draw.line(self.screen, BLACK,
                           (rect.centerx, rect.top), (rect.centerx, rect.bottom), 2)
            # Border
            pygame.draw.rect(self.screen, BLACK, rect, 4)
            # Check if box is on target (glow effect)
            if (x, y) in self.targets:
                glow_rect = rect.inflate(6, 6)
                pygame.draw.rect(self.screen, GREEN, glow_rect, 3)

        # Draw player (Spidey with spider symbol)
        if self.player_pos:
            x, y = self.player_pos
            center_x = self.offset_x + x * TILE_SIZE + TILE_SIZE // 2
            center_y = self.offset_y + y * TILE_SIZE + TILE_SIZE // 2
            radius = TILE_SIZE // 2 - 5

            # Main body (red and blue split)
            pygame.draw.circle(self.screen, SPIDEY_RED, (center_x, center_y), radius)
            # Blue accent (left side)
            pygame.draw.circle(self.screen, SPIDEY_BLUE, (center_x - radius//3, center_y), radius//2)

            # Draw spider symbol (simple black spider)
            spider_size = radius // 3
            # Spider body
            pygame.draw.circle(self.screen, BLACK, (center_x, center_y), spider_size)
            # Spider legs (4 lines radiating out)
            for angle in [45, 135, 225, 315]:
                rad = math.radians(angle)
                end_x = center_x + int(radius * 0.6 * math.cos(rad))
                end_y = center_y + int(radius * 0.6 * math.sin(rad))
                pygame.draw.line(self.screen, BLACK, (center_x, center_y), (end_x, end_y), 3)

            # Outer border
            pygame.draw.circle(self.screen, BLACK, (center_x, center_y), radius, 3)

        # Draw level indicator and move counter
        font_small = pygame.font.Font(None, 36)
        level_text = font_small.render(f"Level {self.current_level + 1}/{len(self.levels)}", True, BLACK)
        self.screen.blit(level_text, (20, 20))

        moves_text = font_small.render(f"Moves: {self.move_count}", True, BLACK)
        self.screen.blit(moves_text, (20, 55))

        # Draw victory message if level complete
        if self.level_complete:
            # Draw animated stars/sparkles
            import random
            random.seed(42)  # Fixed seed for consistent star positions
            for i in range(20):
                # Calculate star position with slight animation
                star_x = random.randint(50, WINDOW_WIDTH - 50)
                star_y = random.randint(80, WINDOW_HEIGHT - 80)
                # Animate star size
                pulse = abs((self.victory_frame + i * 10) % 60 - 30) / 30
                star_size = int(3 + pulse * 5)
                # Draw star
                pygame.draw.circle(self.screen, YELLOW, (star_x, star_y), star_size)
                # Draw star points
                for angle in [0, 72, 144, 216, 288]:
                    rad = math.radians(angle + (self.victory_frame % 360))
                    point_x = star_x + int(star_size * 2 * math.cos(rad))
                    point_y = star_y + int(star_size * 2 * math.sin(rad))
                    pygame.draw.line(self.screen, YELLOW, (star_x, star_y), (point_x, point_y), 2)

            # Semi-transparent overlay
            overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
            overlay.set_alpha(200)
            overlay.fill(BLACK)
            self.screen.blit(overlay, (0, 0))

            # Victory text
            font_large = pygame.font.Font(None, 80)
            font_small = pygame.font.Font(None, 40)

            # Check if this is the last level
            is_last_level = self.current_level == len(self.levels) - 1

            if is_last_level:
                victory_text = font_large.render("ALL LEVELS COMPLETE!", True, YELLOW)
            else:
                victory_text = font_large.render("LEVEL COMPLETE!", True, YELLOW)
            victory_rect = victory_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
            self.screen.blit(victory_text, victory_rect)

            # Show appropriate instructions
            restart_text = font_small.render("Press R to restart", True, WHITE)
            restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20))
            self.screen.blit(restart_text, restart_rect)

            if not is_last_level:
                next_text = font_small.render("Press N for next level", True, LIME)
                next_rect = next_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 70))
                self.screen.blit(next_text, next_rect)

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
