# ICS3U
# Assignment 2: Logo
# <Qudrat Fazli>

# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
import pygame
pygame.init()

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (214, 12, 15)
BLUE = (46, 5, 140)

# Set the screen size (please don't change this)
SCREENWIDTH = 400
SCREENHEIGHT = 400

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Logo")

# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False

    # --- Game logic goes here
    # There should be none for a static image
    
    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(WHITE)

    # Queue different shapes and lines to be drawn
    #pygame.draw.rect(screen, RED, [55, 200, 100, 70], 0)
    #pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    pygame.draw.ellipse(screen, RED, [75, 75, 250, 250], 0)
    pygame.draw.ellipse(screen, BLACK, [75, 75, 250, 250], 4)
    pygame.draw.ellipse(screen, WHITE, [100, 100, 200, 200], 0)
    pygame.draw.ellipse(screen, RED, [125, 125, 150, 150], 0)
    pygame.draw.ellipse(screen, BLUE, [143, 143, 115, 115], 0)
    pygame.draw.polygon(screen, WHITE, ([148, 182], [190, 182], [200, 145], [210, 182], [252, 182], [217, 205], [228, 242], [200, 220],[172, 242], [182, 205]    ), 0)
    
    
     

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
