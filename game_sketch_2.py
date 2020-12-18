import pygame
import sys
from pygame import mixer
import model
import pygame.locals

mixer.init()
pygame.init()
FPS = 30

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


class Player:
    """
    Класс отвечает за свойства игроков
    """
    def __init__(self, turn):
        self.score = 0
        self.mistakes = 3
        self.turn = turn
        self.path = model.np.array([], dtype='<U13')


class Game:
    """
    Класс отвечает за интерфейс игры
    """
    def __init__(self, clauses, states, buttons):
        self.clauses = clauses
        self.states = states
        self.buttons = buttons

    def renderrul(self, surface, font, num_buttons):
        """
        Метод отвечает за отображение кнопок в разделе правил
        :param surface: место отображения
        :param font: шрифт
        :param num_buttons: отвечает за цвет кнопок
        :return:
        """
        for i in self.buttons:
            if num_buttons == i[5]:
                surface.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                surface.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def rules(self):
        """
        Метод отвечает за отображение окна с правилами
        :return:
        """
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
                    done = 0
                    continue
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    print(mp)
                    if button == 0:
                        game.menu()
                    elif button == 1:
                        done = True
            window.blit(screen, (0, 0))
            pygame.display.flip()

    def rendermenu(self, surface, font, num_clause):
        """
        Метод отвечает за отображение кнопок в разделе меню
        :param surface: место отображения
        :param font: шрифт
        :param num_clause: отвчает за цвет кнопок
        :return:
        """
        for i in self.clauses:
            if num_clause == i[5]:
                surface.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                surface.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def menu(self):
        """
        Метод отвечает за отображение окна с меню
        :return:
        """
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
                    pygame.quit()
                    sys.exit()
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if clause == 0:
                        self.level_master('Data.txt')
                    elif clause == 1:
                        self.rules()
                    elif clause == 2:
                        pygame.quit()
                        sys.exit()
            window.blit(screen, (0, 0))
            window.blit(info, (70, 0))
            pygame.display.flip()
    
    def _win_blit(self, window, master_file_name, name_file_name, start, stop,
                  lasts):
        """

        :param window:
        :param master_file_name:
        :param name_file_name:
        :param start:
        :param stop:
        :param lasts:
        :return:
        """
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
        
    def _get_text(self, lasts, start_3str, stop_3str):
        """
        Метод отвечает за возможность ввода текста в режиме игры
        :param lasts:
        :param start_3str:
        :param stop_3str:
        :return:
        """
        applicant = ''
        font = pygame.font.Font(None, 52)
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.locals.KEYDOWN:
                    if event.unicode.isalpha():
                        applicant += event.unicode
                    elif event.key == pygame.locals.K_SPACE:
                        applicant += ' '
                    elif event.key == pygame.locals.K_BACKSPACE:
                        applicant = applicant[:-1]
                    elif event.key == pygame.locals.K_RETURN:
                        return applicant
                elif event.type == pygame.QUIT:
                    return 'EXIT'
            self._win_blit(window, 'master.jpg', 'name.png', start_3str,
                           stop_3str, lasts)
            applicant_text = font.render(applicant, True, (251, 243, 0))
            rect = applicant_text.get_rect()
            rect.center = (400, 620)
            window.blit(applicant_text, rect)
            clock.tick(FPS)
            pygame.display.flip()
        
    def _special_event(self, window, file_name):
        screen = pygame.image.load(file_name)
        window.blit(screen, (0, 0))
        pygame.display.update()
        clock.tick(1)
    
    def level_master(self, file_name: str):
        """
        Метод отвечает за отображение окна с режимом игры
        :param file_name:
        :return:
        """
        stell_graph = model.Graph(file_name)
        start_3str, stop_3str = stell_graph.rnd_start_stop()
        current = stell_graph.constellations[start_3str]
        stop = stell_graph.constellations[stop_3str]
        window = pygame.display.set_mode((800, 670))
        pygame.display.set_caption('ASTROWARS')        
        self._win_blit(window, 'master.jpg', 'name.png', start_3str,
                       stop_3str, [])
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
            applicant_str = self._get_text(lasts, start_3str, stop_3str)
            if applicant_str == 'EXIT':
                finished = True
                continue
            applicant = stell_graph.is_neighbours(current, applicant_str)
            if applicant:
                if applicant.mark:
                    current_player.mistakes -= 1
                    self._special_event(window, 'mistake.jpg')
                    clock.tick(1)
                else:
                    current = applicant
                    current_player.path = model.np.append(current_player.path,
                                                          current.names[0])
                    player1.turn = not player1.turn
                    player2.turn = not player2.turn
                    print('Meow')
            else:
                current_player.mistakes -= 1
                self._special_event(window, 'mistake.jpg')
        
            if not current_player.mistakes:
                if current_player is player1:
                    self._special_event(window, 'pl2win.jpg')
                    clock.tick(0.3)
                    finished = 1
                else:
                    self._special_event(window, 'pl1win.jpg')
                    clock.tick(0.3)
                    finished = 1
            if current is stop:
                if current_player is player1:
                    self._special_event(window, 'pl1win.jpg')
                    clock.tick(0.3)
                    finished = 1
                else:
                    self._special_event(window, 'pl2win.jpg')
                    clock.tick(0.3)
                    finished = 1
            pygame.display.update()
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True


# Sound
pygame.mixer.pre_init(44100, -16, 1, 100)
pygame.mixer.init()
sound = pygame.mixer.Sound('starwars.ogg')
sound.play(-1)

game = Game(clauses, states, buttons)
game.menu()
