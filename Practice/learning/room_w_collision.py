import pygame

# Initialize pygame
pygame.init()

# Create the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Collision Example")

# Add the background color
background_color = (1, 139, 1)
screen.fill(background_color)

# Wall colors
wall_color = (139, 69, 19)  # Brown
table_color = (205, 133, 63)  # Tan

# Define walls and objects as rectangles
walls = [
    pygame.Rect(50, 50, 700, 20),  # Top wall
    pygame.Rect(100, 100, 20, 600),  # Left wall
    pygame.Rect(300, 400, 450, 20),  # Middle wall
    pygame.Rect(750, 50, 20, 400),  # Right wall
]

# Define the table
table = pygame.Rect(200, 300, 100, 50)

# Load the cupid image
cupid = pygame.image.load("cupid.png")
cupid = pygame.transform.scale(cupid, (40, 40))  # Resize if needed

# Player starting position
cupid_rect = pygame.Rect(150, 150, 40, 40)  # x, y, width, height

# Movement speed
speed = 5

# Event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Copy the current position to check for collisions later
    new_rect = cupid_rect.copy()

    # Update position based on input
    if keys[pygame.K_LEFT]:
        new_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        new_rect.x += speed
    if keys[pygame.K_UP]:
        new_rect.y -= speed
    if keys[pygame.K_DOWN]:
        new_rect.y += speed

    # Collision detection
    collision = False
    for wall in walls:
        if new_rect.colliderect(wall):
            collision = True
            break
    if new_rect.colliderect(table):
        collision = True
        
    # If no collision, update the player position
    if not collision:
        cupid_rect = new_rect

    # Redraw the screen
    screen.fill(background_color)
    for wall in walls:
        pygame.draw.rect(screen, wall_color, wall)
    pygame.draw.rect(screen, table_color, table)

    # Draw the player
    screen.blit(cupid, (cupid_rect.x, cupid_rect.y))

    # Update the display
    pygame.display.flip()

pygame.quit()