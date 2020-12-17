import model
import numpy as np
import pygame
import sys
import tkinter as t
import pygame.locals


pygame.init()

FPS = 20

stell_graph = model.Graph('Data.txt')
start_3str, stop_3str = stell_graph.rnd_start_stop()
current = start_3str

window = pygame.display.set_mode((800, 670))
screen = pygame.Surface((800, 670))

pygame.display.set_caption('ASTROWARS')

def win_blit(window, master_file_name, name_file_name, start, stop):
    screen = pygame.image.load(master_file_name)
    info = pygame.image.load(name_file_name)
    window.blit(screen, (0, 150))
    window.blit(info, (70, 0))
    
    f = pygame.font.Font(None, 48)
    start_text = f.render(start, True, (251, 243, 0))
    window.blit(start_text, (150, 186))
    stop_text = f.render(stop, True, (251, 243, 0))
    window.blit(stop_text, (94, 237))

def get_text():
    applicant = ''
    font = pygame.font.Font(None, 52)
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.locals.KEYDOWN:
                if event.unicode.isalpha():
                    applicant += event.unicode
                elif event.key == pygame.locals.K_BACKSPACE:
                    applicant = applicant[:-1]
                elif event.key == pygame.locals.K_RETURN:
                    return applicant
            elif event.type == pygame.QUIT:
                return 'EXIT'
        win_blit(window, 'master.jpg', 'name.png', start_3str, stop_3str)
        applicant_text = font.render(applicant, True, (251, 243, 0))
        rect = applicant_text.get_rect()
        rect.center = (400, 620)
        window.blit(applicant_text, rect)
        clock.tick(FPS)
        pygame.display.flip()

win_blit(window, 'master.jpg', 'name.png', start_3str, stop_3str)

pygame.display.flip()

clock = pygame.time.Clock()
finished = False

path1 = []
path2 = []


while not finished:
    applicant = get_text()
    if applicant == 'EXIT':
        finished = True
    
    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()