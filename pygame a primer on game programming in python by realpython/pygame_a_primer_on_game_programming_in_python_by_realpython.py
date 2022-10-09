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
#moved Player recipe here
class Player(pygame.sprite.Sprite):
    def __init__(self):
       super(self,Player,surf)
       self.surf = pygame.Surface((75,25))
       self.surf.fill((255,255,255))
       self.rect= self.surf.get_rect()

SCREEN_WIDTH=800
SCREEN_HEIGHT=600



pygame.init()

screen=pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running=True

while running:
   for event in pygame.event.get():
       if event.type==KEYDOWN:
           if event.key==K_ESCAPE:
               running=False
       elif event.type==QUIT:
           running=False
#moved screen.fill(()), screen.blit, pygame.display.flip() here
    screen.fill((255, 255, 255))
    screen.blit(Player,surf((SCREEN_WIDTH/2,SCREEN_HEIGHT/2)))
    pygame.display.flip()
pygame.quit()