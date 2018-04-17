# ICS3U
# Assignment 2: Action
# <Qudrat Fazli>

# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
# Don't forget to import your class
import pygame, random
from Bubbles import BUBBLES
pygame.init()

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (197, 201, 201)
Ocean = (50, 115, 219)

# Set the screen size
SCREENWIDTH = 400
SCREENHEIGHT = 400

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Animation")
all_sprites_list = pygame.sprite.Group()

for i in range(20):
    Bubble1 = BUBBLES(BLUE, 10, 10, random.randint(5,15))
    Bubble1.rect.x = random.randint(400,0)
    Bubble1.rect.y = randint(400,0)
    all_sprites_list.add(Bubble1)
    

all_sprites_list.add(Bubble1)

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
    for Bubbles in BUBBLES:
        Buubles.moveForward(5)
        if Bubbles.rect.y < SCREENHEIGHT:
            Buubles.changeSpeed(random.randint(5,20))
            Bubbles.rect.y = 600
            Bubbles.rect.x = random.randint(400,0)
    # --- Game logic goes here
    # There should be none for a static image
    
    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(WHITE)

    # Queue different shapes and lines to be drawn
    # pygame.draw.rect(screen, RED, [55, 200, 100, 70], 0)
    # pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    # pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
