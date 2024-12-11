# Import the pygame module
import pygame

# initialize all of the necessary modules of Pygame
pygame.init()


# create the main window
screen = pygame.display.set_mode()

# fill the screen blank
screen.fill(())
"""
Example: pygame.display.set_mode((800, 600)) creates an 800x600 pixel window.
Using double parentheses ensures that the argument is passed as a single tuple, which is the expected
format for specifying the size of the display window in Pygame. 

"""
# Sets the title of the game window.
pygame.display.set_caption()


# Update contents of entire window
pygame.display.update()

# Use pygame.key.get_pressed() to detect arrow key presses.



# Update specific area of window
pygame.display.flip()

# Fetch all user generated events (like key presses, and mouse movements)
pygame.event.get()

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False

# Close the game window and clean up Pygame resources
pygame.quit()

