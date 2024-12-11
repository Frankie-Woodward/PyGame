import pygame

# initialize pygame
pygame.init()

# DRAWING A RED RECTANGLE TO THE SCREEN USING pygame.draw.rect() 

# create the game window screen
# screen = pygame.display.set_mode((400,300))
# pygame.display.set_caption("rectangle test")

# # fill background is recommended, Pygame does not automatically clear the screen between frames.
# screen.fill((0,0,0))

# # draw the rectangle
# pygame.draw.rect(screen, (200, 0, 0), (50, 50, 100, 100)) #red rectangle

# # update the display to make changes visible
# pygame.display.flip()

# # add event loop to keep the window open
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

# # quit pygame cleanly
# pygame.quit()


# DRAWING A CIRCLE TO THE SCREEN USING pygame.draw.circle()

# game window screen
# screen = pygame.display.set_mode((400, 300))
# pygame.display.set_caption("circle test")

# # fill the screen blank
# screen.fill((0,0,0))

# # draw the circle
# pygame.draw.circle(screen, (0,255,0), (150,150), 50) #green circle

# # update the display
# pygame.display.flip()

# # event loop to keep the window open
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

# pygame.quit()

# LOADING AN IMAGE TO THE SCREEN USING pygame.image.load()

# create the game window
# screen = pygame.display.set_mode((500, 500))
# pygame.display.set_caption("Imade Loading Game")

# # fill the screen blank
# screen.fill((0,0,0))

# # load the image, Pygame requires loading images before using them to prevent crashes.
# image = pygame.image.load("cupid.png")

# # manually resizing the image
# original_width, original_height = image.get_size()


# # Step 5: Calculate the new dimensions (quarter of the size)
# new_width = original_width // 8
# new_height = original_height // 8

# # Step 6: Resize the image
# resized_image = pygame.transform.scale(image, (new_width, new_height))

# # Draw the image on the screen using blit or "screen.blit"
# screen.blit(resized_image, (100, 100))

# # update the display
# pygame.display.flip()

# # create the event loop to prevent the screen from closing unless user closes window
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

# pygame.quit()

# ADDING SOUND TO YOUR GAME

sound = pygame.mixer.Sound("beep.wav")

sound.play(5)

pygame.time.delay(2000)

pygame.quit()

