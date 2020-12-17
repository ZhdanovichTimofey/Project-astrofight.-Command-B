import model
import numpy as np
import pygame
import sys
import tkinter as t
import random

def rnd_start_stop (graph:model.Graph):
    a = 0

pygame.init()

FPS = 60

stell_graph = model.Graph('Data.txt')

window = pygame.display.set_mode((800, 670))
screen = pygame.Surface((800, 670))

pygame.display.set_caption('ASTROWARS')

screen = pygame.image.load('master.jpg')
info = pygame.image.load('name.png')
window.blit(screen, (0, 150))
window.blit(info, (70, 0))
pygame.display.flip()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()