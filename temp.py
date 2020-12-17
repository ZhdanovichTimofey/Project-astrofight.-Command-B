import model
import numpy as np
import pygame
import sys
import tkinter as t




pygame.init()

FPS = 60

stell_graph = model.Graph('Data.txt')
start_3str, stop_3str = stell_graph.rnd_start_stop()

window = pygame.display.set_mode((800, 670))
screen = pygame.Surface((800, 670))

pygame.display.set_caption('ASTROWARS')

screen = pygame.image.load('master.jpg')
info = pygame.image.load('name.png')
window.blit(screen, (0, 150))
window.blit(info, (70, 0))

f = pygame.font.Font(None, 48)
start_text = f.render(start_3str, True, (251, 243, 0))
window.blit(start_text, (150, 186))
stop_text = f.render(stop_3str, True, (251, 243, 0))
window.blit(stop_text, (94, 237))

pygame.display.flip()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

path1 = []
path2 = []


while not finished:
    
    
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()