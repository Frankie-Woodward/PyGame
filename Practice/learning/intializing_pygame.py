# Import the pygame module
import pygame

# initialize all of the necessary modules of Pygame
pygame.init()

# create the main window
pygame.display.set_mode()
"""
Example: pygame.display.set_mode((800, 600)) creates an 800x600 pixel window.
Using double parentheses ensures that the argument is passed as a single tuple, which is the expected
format for specifying the size of the display window in Pygame. 

"""
# Sets the title of the game window.
pygame.display.set_caption()

# Fetch all user generated events (like key presses, and mouse movements)
pygame.event.get()

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False




# Close the game window and clean up Pygame resources
pygame.quit()