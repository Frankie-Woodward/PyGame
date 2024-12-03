import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer Game")
clock = pygame.time.Clock()

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = SCREEN_HEIGHT - 70
        self.velocity_y = 0
        self.is_jumping = False

    def update(self, platforms):
        # Gravity
        self.velocity_y += 1
        if self.velocity_y > 10:
            self.velocity_y = 10
        self.rect.y += self.velocity_y

        # Check for platform collisions
        hit_list = pygame.sprite.spritecollide(self, platforms, False)
        for platform in hit_list:
            if self.velocity_y > 0:  # Falling
                self.rect.bottom = platform.rect.top
                self.velocity_y = 0
                self.is_jumping = False

    def move(self, dx):
        self.rect.x += dx

    def jump(self, platforms):
        # Allow jump only if not in the air
        hit_list = pygame.sprite.spritecollide(self, platforms, False)
        if not self.is_jumping and hit_list:
            self.velocity_y = -15
            self.is_jumping = True

# Platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# Create sprite groups
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()

# Create platforms
platform_data = [
    (0, SCREEN_HEIGHT - 20, SCREEN_WIDTH, 20),  # Ground
    (150, 520, 100, 20),
    (300, 480, 150, 20),
    (500, 450, 200, 20),
]

for data in platform_data:
    platform = Platform(*data)
    platforms.add(platform)
    all_sprites.add(platform)

# Create the player
player = Player()
all_sprites.add(player)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move(-5)
    if keys[pygame.K_RIGHT]:
        player.move(5)
    if keys[pygame.K_UP]:
        player.jump(platforms)

    # Update player and redraw screen
    player.update(platforms)
    screen.fill(WHITE)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()