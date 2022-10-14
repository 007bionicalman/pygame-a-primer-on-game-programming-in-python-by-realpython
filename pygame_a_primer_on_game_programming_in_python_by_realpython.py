#exercise 1
#import pygame
#pygame.init()

#screen=pygame.display.set_mode((500,500))
#pygame.display.set_caption("exersise 1:hello world")

#running=True
#while running:

    #for event in pygame.event.get():
        #if event.type==pygame.QUIT:
            #running=False

    #screen.fill ((255,255,255))

    #pygame.draw.circle(screen, (0,0,255), (250,250),75)

    #pygame.display.flip()

#pygame.quit()

#exercise 2
#does not exit when one pushes escape
import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

SCREEN_WIDTH=800
SCREEN_HEIGHT=600

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("exersise 2")

running=True

while running:
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False

    pygame.display.flip()


#exercise 3
# Import the pygame module
#import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
#from pygame.locals import (
    #K_UP,
    #K_DOWN,
    #K_LEFT,
    #K_RIGHT,
    #K_ESCAPE,
    #KEYDOWN,
    #QUIT,
#)

# Define constants for the screen width and height
#SCREEN_WIDTH = 800
#SCREEN_HEIGHT = 600
#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#pygame.display.set_caption("exercise 3: My First Sprite Player Ever")

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
#class Player(pygame.sprite.Sprite):
    #def __init__(self):
        #super(Player, self).__init__()
        #self.surf = pygame.Surface((75, 25))
        #self.surf.fill((255, 255, 255))
        #self.rect = self.surf.get_rect()

# Initialize pygame
#pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Instantiate player. Right now, this is just a rectangle.
#player = Player()

# Variable to keep the main loop running
#running = True

# Main loop
#while running:
    # for loop through the event queue
    #for event in pygame.event.get():
        # Check for KEYDOWN event
        #if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            #if event.key == K_ESCAPE:
                #running = False
        # Check for QUIT event. If QUIT, then set running to false.
        #elif event.type == QUIT:
            #running = False

    # Fill the screen with black
    #screen.fill((0, 0, 0))

    # Draw the player on the screen
    #0

    # Update the display
    #pygame.display.flip()"""