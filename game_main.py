import pygame
import sys
from pygame import mixer

mixer.init()
pygame.init()

window = pygame.display.set_mode((800, 670))
screen = pygame.Surface((800, 670))
clock = pygame.time.Clock()

pygame.display.set_caption('ASTROWARS')

# Menu Description
clauses = [(350, 260, u'Play', (11, 0, 77), (250, 250, 30), 0),
           (350, 300, u'Rules', (11, 0, 77), (250, 250, 30), 1),
           (350, 340, u'Exit', (11, 0, 77), (250, 250, 30), 2)]
states = [(300, 300, u'Beginner', (11, 0, 77), (250, 250, 30), 0),
          (300, 340, u'Master', (11, 0, 77), (250, 250, 30), 1),
          (50, 600, u'Menu', (11, 0, 77), (250, 250, 30), 2)]
buttons = [(50, 600, u'Menu', (11, 0, 77), (250, 250, 30), 0),
           (150, 600, 'Retry', (0, 0, 0), (0, 0, 0), 1)]


def level_master():
    screen = pygame.image.load('starsky.jpg')
    info = pygame.image.load('name.png')
    window.blit(screen, (0, 150))
    window.blit(info, (70, 0))
    pygame.display.flip()


def level_beginner():
    screen = pygame.image.load('starsky.jpg')
    info = pygame.image.load('name.png')
    window.blit(screen, (0, 150))
    window.blit(info, (70, 0))
    pygame.display.flip()


# Menu
class Menu:
    def __init__(self, clauses, states, buttons):

        self.clauses = clauses
        self.states = states
        self.buttons = buttons

    def renderrul(self, surface, font, num_buttons):
        for i in self.buttons:
            if num_buttons == i[5]:
                surface.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                surface.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def rules(self):
        done = True
        font_rules = pygame.font.Font(None, 50)
        pygame.key.set_repeat(0, 0)
        pygame.mouse.set_visible(True)
        while done:
            button = 1
            screen = pygame.image.load('rules.jpg')
            mp = pygame.mouse.get_pos()
            for i in self.buttons:
                if (i[0] < mp[0] < i[0] + 155) and (i[1] < mp[1] < i[1] + 50):
                    button = i[5]
            self.renderrul(screen, font_rules, button)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    print(mp)
                    if button == 0:
                        game.menu()
                    elif button == 1:
                        done = True
            window.blit(screen, (0, 0))
            pygame.display.flip()

    def rendermenu(self, surface, font, num_clause):
        for i in self.clauses:
            if num_clause == i[5]:
                surface.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                surface.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def menu(self):
        done = True
        font_menu = pygame.font.Font(None, 50)
        pygame.key.set_repeat(0, 0)
        pygame.mouse.set_visible(True)
        clause = 0
        while done:
            screen = pygame.image.load('starsky.jpg')
            info = pygame.image.load('name.png')
            mp = pygame.mouse.get_pos()
            for i in self.clauses:
                if (i[0] < mp[0] < i[0] + 155) and (i[1] < mp[1] < i[1] + 50):
                    clause = i[5]
            self.rendermenu(screen, font_menu, clause)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if clause == 0:
                        self.chooselevel()
                    elif clause == 1:
                        self.rules()
                    elif clause == 2:
                        sys.exit()
            window.blit(screen, (0, 0))
            window.blit(info, (70, 0))
            pygame.display.flip()

    # Choose level (mode)
    def renderchoose(self, surface, font, num_states):
        for i in self.states:
            if num_states == i[5]:
                surface.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                surface.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def chooselevel(self):
        done = True
        font_choose = pygame.font.Font(None, 50)
        pygame.key.set_repeat(0, 0)
        pygame.mouse.set_visible(True)
        state = 0
        while done:
            screen = pygame.image.load('choose.jpg')
            mp = pygame.mouse.get_pos()
            for i in self.states:
                if (i[0] < mp[0] < i[0] + 155) and (i[1] < mp[1] < i[1] + 50):
                    state = i[5]
            self.renderchoose(screen, font_choose, state)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if state == 0:
                        level_beginner()
                    elif state == 1:
                        level_master()
                    elif state == 2:
                        game.menu()
            window.blit(screen, (0, 0))
            pygame.display.flip()

# Sound
pygame.mixer.pre_init(44100, -16, 1, 100)
pygame.mixer.init()
sound = pygame.mixer.Sound('starwars.ogg')
sound.play(-1)


game = Menu(clauses, states, buttons)
game.menu()
