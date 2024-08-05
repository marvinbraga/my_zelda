import random
import sys

import pygame

# Initialize Pygame
pygame.init()

# Set up the game window dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set up the title of the game
pygame.display.set_caption("LifeCycle")

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Set up the grid dimensions
GRID_SIZE = 20
grid_width = SCREEN_WIDTH // GRID_SIZE
grid_height = SCREEN_HEIGHT // GRID_SIZE

# Create the game grid
grid = [[0 for _ in range(grid_width)] for _ in range(grid_height)]


# Function to draw the grid
def draw_grid():
    for i in range(grid_width):
        for j in range(grid_height):
            pygame.draw.rect(screen, WHITE, (i * GRID_SIZE, j * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)


# Define the player's starting position
player_x = random.randint(0, grid_width - 1)
player_y = random.randint(0, grid_height - 1)

# Define the player's sprite
player_sprite = pygame.Surface((GRID_SIZE, GRID_SIZE))
player_sprite.fill(WHITE)

# Add obstacles to the grid
obstacles = []
obstacle_colors = [RED, GREEN, BLUE, YELLOW]
for _ in range(10):
    obstacle_x = random.randint(0, grid_width - 1)
    obstacle_y = random.randint(0, grid_height - 1)
    obstacle_color = random.choice(obstacle_colors)
    obstacles.append((obstacle_x, obstacle_y, obstacle_color))


# Function to draw the player and obstacles
def draw_player_and_obstacles():
    screen.blit(player_sprite, (player_x * GRID_SIZE, player_y * GRID_SIZE))
    for obstacle in obstacles:
        pygame.draw.rect(screen, obstacle[2], (obstacle[0] * GRID_SIZE, obstacle[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))


# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_y -= 1
            elif event.key == pygame.K_DOWN:
                player_y += 1
            elif event.key == pygame.K_LEFT:
                player_x -= 1
            elif event.key == pygame.K_RIGHT:
                player_x += 1

    # Update the game state
    screen.fill(BLACK)
    draw_grid()
    draw_player_and_obstacles()

    # Check for collisions
    for obstacle in obstacles:
        if player_x == obstacle[0] and player_y == obstacle[1]:
            print("Game Over!")
            pygame.quit()
            sys.exit()

    # Update the screen
    pygame.display.flip()
    pygame.time.Clock().tick(60)
