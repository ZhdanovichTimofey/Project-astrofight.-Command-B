import model
import numpy as np
import pygame
import sys
import tkinter as t
import pygame.locals

class Player:
    def __init__(self, turn):
        self.score = 0
        self.mistakes = 3
        self.turn = turn
        self.path = np.array([], dtype = '<U13')

pygame.init()

FPS = 20

stell_graph = model.Graph('Data.txt')
start_3str, stop_3str = stell_graph.rnd_start_stop()
current = stell_graph.constellations[start_3str]
stop = stell_graph.constellations[stop_3str]

window = pygame.display.set_mode((800, 670))

pygame.display.set_caption('ASTROWARS')

def win_blit(window, master_file_name, name_file_name, start, stop, lasts):
    screen = pygame.image.load(master_file_name)
    info = pygame.image.load(name_file_name)
    window.blit(screen, (0, 150))
    window.blit(info, (70, 0))
    
    f = pygame.font.Font(None, 48)
    start_text = f.render(start, True, (251, 243, 0))
    window.blit(start_text, (150, 186))
    stop_text = f.render(stop, True, (251, 243, 0))
    window.blit(stop_text, (94, 237))
    try:
        last1 = f.render(lasts[0], True, (251, 243, 0))
        window.blit(last1, (150, 370))
    except IndexError:
        pass
    try:
        last2 = f.render(lasts[1], True, (251, 243, 0))
        window.blit(last2, (530, 370))
    except IndexError:
        pass

def get_text(lasts, start_3str, stop_3str):
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
        win_blit(window, 'master.jpg', 'name.png', start_3str, stop_3str, lasts)
        applicant_text = font.render(applicant, True, (251, 243, 0))
        rect = applicant_text.get_rect()
        rect.center = (400, 620)
        window.blit(applicant_text, rect)
        clock.tick(FPS)
        pygame.display.flip()
        
def special_event(window, file_name):
    screen = pygame.image.load(file_name)
    window.blit(screen, (0, 0))
    pygame.display.update()

win_blit(window, 'master.jpg', 'name.png', start_3str, stop_3str, [])

pygame.display.flip()

clock = pygame.time.Clock()
finished = False

player1 = Player(True)
player2 = Player(False)

while not finished:
    lasts = []
    try:
        lasts.append(player1.path[len(player1.path) - 1])
    except IndexError:
        pass
    try:
        lasts.append(player2.path[len(player2.path) - 1])
    except IndexError:
        pass
    current.mark = 1
    if player1.turn:
        current_player = player1
    else:
        current_player = player2
    applicant_str = get_text(lasts, start_3str, stop_3str)
    if applicant_str == 'EXIT':
        finished = True
        continue
    applicant = stell_graph.is_neighbours(current, applicant_str)
    if applicant:
        if applicant.mark:
            current_player.mistakes -= 1
            special_event(window, 'mistake.jpg')
            clock.tick(1)
        else:
            current = applicant
            current_player.path = np.append(current_player.path, 
                                            current.names[0])
            player1.turn = not player1.turn
            player2.turn = not player2.turn
            print('Meow')
    else:
        current_player.mistakes -= 1
        special_event(window, 'mistake.jpg')
        clock.tick(1)
        
    if not current_player.mistakes:
        if current_player is player1:
            special_event(window, 'pl2win.jpg')
            clock.tick(0.2)
            finished = 1
        else:
            special_event(window, 'pl1win.jpg')
            clock.tick(0.2)
            finished = 1
    if current is stop:
        if current_player is player1:
            special_event(window, 'pl1win.jpg')
            clock.tick(0.2)
            finished = 1
        else:
            special_event(window, 'pl2win.jpg')
            clock.tick(0.2)
            finished = 1
    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()