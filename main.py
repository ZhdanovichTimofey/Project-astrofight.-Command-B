import sys
import os
import pygame
from model import *
from menu import *
pygame.init()

game = Menu(punkts)
game.menu()

done = True
pygame.key.set_repeat(1, 1)
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                game.menu()

        if e.type == pygame.MOUSEMOTION:
            pygame.mouse.set_visible(False)
            p = pygame.mouse.get_pos()

    y = -300
    x = -200

    screen = pygame.image.load('starsky.jpg')
    info = pygame.image.load('name.png')

    screen.blit(end.render('Game Over', 1, (210, 120, 200)), (200, y))
    screen.blit(again.render('Try again?(press Space)', 1, (210, 120, 200)),
                (200, x))
    info.blit(lifes_f.render('Lifes: ' + str(lifes), 1, (210, 120, 200)),
              (600, 0))
    window.blit(info, (0, 0))
    window.blit(screen, (0, 30))
    pygame.display.flip()
    pygame.time.delay(5)