import pygame

# Initialize pygame
pygame.init()

# create the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Example of Lair")

# add the background color
background_color = (1, 139, 1)
screen.fill(background_color)

# add tables and walls
wall_color = (139, 69, 19)  # Brown for walls
table_color = (205, 133, 63)  # Tan for tables

# Step 2: Draw the objects
pygame.draw.rect(screen, wall_color, (50, 50, 700, 20))  # Top wall
pygame.draw.rect(screen, table_color, (200, 300, 100, 50))  # Table
pygame.draw.rect(screen, wall_color, (100, 100, 20, 600))  # left wall
pygame.draw.rect(screen, wall_color, (300, 400, 450, 20))  # middle wall
pygame.draw.rect(screen, wall_color, (750, 50, 20, 400))  # right wall

# Step 1: Load the cupid image
cupid = pygame.image.load("cupid.png")

# Step 2: Scale if needed (resize to 40x40 for example)
cupid = pygame.transform.scale(cupid, (40, 40))

# Step 3: Define starting position
cupid_x, cupid_y = 100, 100

# Step 4: Draw the cupid onto the screen
screen.blit(cupid, (cupid_x, cupid_y))

# Use pygame.key.get_pressed() to detect arrow key presses.
# Define movement speed
speed = 5


# update the display
pygame.display.flip()

# event loop

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # handle the key inputs to move the character
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        cupid_x -= speed
    if keys[pygame.K_RIGHT]:
        cupid_x += speed
    if keys[pygame.K_UP]:
        cupid_y -= speed
    if keys[pygame.K_DOWN]:
        cupid_y += speed

    # refresh the screen background for player movement
    screen.fill(background_color)
    # Step 2: Draw the objects
    pygame.draw.rect(screen, wall_color, (50, 50, 700, 20))  # Top wall
    pygame.draw.rect(screen, table_color, (200, 300, 100, 50))  # Table
    pygame.draw.rect(screen, wall_color, (100, 100, 20, 600))  # left wall
    pygame.draw.rect(screen, wall_color, (300, 400, 450, 20))  # middle wall
    pygame.draw.rect(screen, wall_color, (750, 50, 20, 400))  # right wall

    # redraw updated cupid in new spot
    screen.blit(cupid, (cupid_x, cupid_y))

    # finally we update the display
    pygame.display.flip()

pygame.quit()