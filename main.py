import pygame
from game import Game
from menu import Menu

# Parte genérica do código.

class Main:

    def __init__(self):                         # Variáveis criadas.

        self.window = pygame.display.set_mode([1280, 720])
        self.title = pygame.display.set_caption('Flappy Dragon')
        self.loop = True
        self.fps = pygame.time.Clock()
        self.game = Game()
        self.menu = Menu()

    def events(self):
        for events in pygame.event.get():       # Controle da janela do jogo.
            if events.type == pygame.QUIT:
                pygame.quit()
                self.loop = False
            if not self.menu.change_scene:
                self.menu.events(events)

    def draw(self):                             # Visualização das imagens na tela.
        if not self.menu.change_scene:
            self.menu.draw(self.window)
            self.menu.update(str(self.game.max_score))

        elif not self.game.change_scene:
            self.game.draw(self.window)
            self.game.update()

        else:
            self.loop = False

    def update(self):                           # Atualização das funções.
        while self.loop:
            self.fps.tick(30)
            self.events()
            self.draw()
            pygame.display.update()

# Reiniciar o jogo.

loop = True
while loop:
    Main().update()