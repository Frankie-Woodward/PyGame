import pygame
import sys

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 40

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Escape")

maze = [
   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
   [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
   [1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
   [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
   [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
   [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
   [1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
   [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
   [1, 1, 1, 1, 1, 1, 1, 1, 3, 1],
]

player_pos = [1, 1]  # Starting row and column

def draw_maze():
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            x = col * TILE_SIZE
            y = row * TILE_SIZE

            if maze[row][col] == 1:
                pygame.draw.rect(screen, BLACK, (x, y, TILE_SIZE, TILE_SIZE))
            elif maze[row][col] == 3:
                pygame.draw.rect(screen, GREEN, (x, y, TILE_SIZE, TILE_SIZE))

    # Draw player
    px, py = player_pos[1] * TILE_SIZE, player_pos[0] * TILE_SIZE
    pygame.draw.rect(screen, RED, (px, py, TILE_SIZE, TILE_SIZE))

def move_player(dx, dy):
    new_x = player_pos[0] + dy
    new_y = player_pos[1] + dx

    # Check boundaries and collisions
    if maze[new_x][new_y] != 1:  # Not a wall
        player_pos[0] = new_x
        player_pos[1] = new_y


running = True
while running:
    screen.fill(WHITE)

    # Draw the maze and player
    draw_maze()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_player(0, -1)
            elif event.key == pygame.K_DOWN:
                move_player(0, 1)
            elif event.key == pygame.K_LEFT:
                move_player(-1, 0)
            elif event.key == pygame.K_RIGHT:
                move_player(1, 0)

    # Check if the player reaches the exit
    if maze[player_pos[0]][player_pos[1]] == 3:
        print("You escaped the maze!")
        running = False

    pygame.display.flip()

pygame.quit()
sys.exit()