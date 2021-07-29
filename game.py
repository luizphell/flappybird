from  obj import Obj, Pipe, Coin, Dragon, Text
import pygame
import random

class Game:

    def __init__(self):                      # Adicionar as variáveis.

        self.all_sprites = pygame.sprite.Group()
        self.coin_group = pygame.sprite.Group()
        self.pipes_group = pygame.sprite.Group()

        self.field = Obj('Flappy_Image/landscape-1769052_1280.png', 0, 0, self.all_sprites)
        self.field2 = Obj('Flappy_Image/landscape-1769052_1280.png', 1280, 0, self.all_sprites)
        self.dragon = Dragon('Flappy_Image/Dragon0.png', 550, 350, self.all_sprites)
        self.score = Text(100, '0')
        self.change_scene = False
        self.time = 0
        self.timer = 0

        self.max_score = 0
        self.check_score()

    def draw(self, window):                 # Desenhar as imagens na janela do jogo.
        self.all_sprites.draw(window)
        self.score.draw(window, 640, 50)

    def update(self):                       # Função de atualização.
        self.move_field()

        if self.dragon.play:
            self.spaw_pipes()
            self.dragon.colision_pipes(self.pipes_group)
            self.dragon.colision_coin(self.coin_group)
            self.score.text_update(str(self.dragon.pts))
            self.all_sprites.update()
        else:
            self.save_score()
            self.gameover()

    def move_field(self):                   # Movimento do cenário.
        self.field.rect[0] -= 3
        self.field2.rect[0] -= 3

        if self.field.rect[0] <= -1280:
            self.field.rect[0] = 0
        if self.field2.rect[0] <= 0:
            self.field2.rect[0] = 1280

    def spaw_pipes(self):                   # Obstáculos em movimento.
        self.time += 1

        if self.time >= random.randrange(90, 300):
            self.time = 0
            pipe = Pipe('Flappy_Image/Pipe1.png', 1280, random.randrange(400, 550), self.all_sprites, self.pipes_group)
            pipe2 = Pipe('Flappy_Image/Pipe2.png', 1280, pipe.rect[1] - 620, self.all_sprites, self.pipes_group)
            coin = Coin('Flappy_Image/0.png', 1300, pipe.rect[1] - 150, self.all_sprites, self.coin_group)

    def gameover(self):
        self.timer += 1
        if self.timer >= 30:
            self.change_scene = True

    def save_score(self):                    # Função de checar od valores do score exibido no menu.
        if self.dragon.pts > self.max_score:
            self.max_score = self.dragon.pts
            var = open('save.txt', 'w')
            var.write(str(self.max_score))
            var.close()

    def check_score(self):
        var = open('save.txt', 'r')
        self.max_score = int(var.read())
        var.close()