# ICS3U
# Assignment 2: Action
# <Qudrat Fazli>

# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
# Don't forget to import your class
import pygame, random
from Bubbles import BUBBLE

pygame.init()
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load('SpongeBob.mp3')#https://www.youtube.com/watch?v=vE2ETqUGj6Q
pygame.mixer.music.play(-1)
BackGround = pygame.image.load('jajaja_400x400.jpg')#https://twitter.com/krustykrabtw
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
speed = 1
Bub = pygame.sprite.Group()

for i in range(20):
    Bubble1 = BUBBLE(BLUE,10,10,random.randint(2,5))
    Bubble1.rect.x = random.randint(0,400)
    Bubble1.rect.y = random.randint(0, 400)
    Bub.add(Bubble1)

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
    for Bubbles in Bub:
        Bubbles.moveUp(speed)
        if Bubbles.rect.y == 0:
            Bubbles.changeSpeed(random.randint(5,20))
            Bubbles.rect.y = 400
            Bubbles.rect.x = random.randint(0,400)
    # --- Game logic goes here
    # There should be none for a static image
    
    # --- Draw code goes here

    # Clear the screen to white
    screen.blit(BackGround,(0, 0))
    Bub.draw(screen)

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
