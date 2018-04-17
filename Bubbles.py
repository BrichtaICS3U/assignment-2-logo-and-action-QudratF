import pygame
WHITE = (255, 255, 255)
 
class BUBBLE(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.
 
    def __init__(self, color, width, height, speed):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
 
        #Initialise attributes of the car.
        self.width=width
        self.height=height
        self.color = color
        self.speed = speed
 
        # Draw the car (a rectangle!)
        pygame.draw.elipse(self.image, self.color, [0, 0, self.width, self.height])
        
        self.elipse = self.image.get_elipse()
 
    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20
        
    def changeSpeed(self, speed):
        self.speed = speed
