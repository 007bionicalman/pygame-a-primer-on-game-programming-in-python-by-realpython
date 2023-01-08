#Controlls: arrow keys up, down, right & left

import pygame

pygame.init()

screen = pygame.display.set_mode([1000, 1000])

running = True

x = 500
y = 500

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -=10
            if event.key == pygame.K_RIGHT:
                x +=10
            if event.key == pygame.K_UP:
                y -=10
            if event.key == pygame.K_DOWN:
                y +=10

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 255), (x, y), 75)

    print (str("x : {} , y : {}").format(x,y) )

    pygame.display.flip()

pygame.quit()