#Import the pygame module.
import pygame
#Import pygame.locals for easier access to key coordinates.
#Updated to conform to flake8 and black standards.
#What is flake8?
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
#Define the constants for the screen width and height.
SCREEN_WIDTH=800
SCREEN_HEIGHT=600
#Define a Player object by extending pygame.sprite.Sprite
#The surface drawn on the screen is now an attribute of 'player'.
#Moved the Player recipe here.
class Player(pygame.sprite.Sprite):
    def __init__(self):
       super(self).__init__()
       self.surf = pygame.Surface((75,25))
       self.surf.fill((255,255,255))
       self.rect= self.surf.get_rect()
#Initialize pygame.
pygame.init()
#Create the screen object. 
#The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT.
screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#Instantiate player. Right now, this is just a rectangle.
player=Player()
#Variable to keep the main loop running.
running=True
#Main loop.
while running:
   #For loop through the event queue.
   for event in pygame.event.get():
       #Check for KEYDOWN event.
       if event.type==KEYDOWN:
           #If the esc key is pressed, then exit the main loop.
           if event.key==K_ESCAPE:
              running=False
       #Check for Quit event. If QUIT, then set running to False.
       elif event.type==QUIT
            running=False
        #Fill the screen black.
        screen.fill((0, 0, 0))
        #Draw the Player on the screen
        screen.blit(player.surf,((SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
        #Update the display
        pygame.display.flip()   