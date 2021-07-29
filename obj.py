import pygame

# Objeto criado para inserir os itens do cenário.

class Obj(pygame.sprite.Sprite):

    def __init__(self, image, x, y,  *groups):
        super().__init__(*groups)

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y

# Objeto com movimento.

class Pipe(Obj):

    def __init__(self, image, x, y, *groups):       # Recebe as mesmas características do Obj.
        super().__init__(image, x, y, *groups)

    def update(self, *args):
        self.move()

    def move(self):                 # Movimento dos canos.
        self.rect[0] -= 3           # Velocidade.

        if self.rect[0] <= -100:
            self.kill()

# Adicionar a recompensa.

class Coin(Obj):

    def __init__(self, image, x, y, *groups):
        super().__init__(image, x, y, *groups)

        self.time = 0

    def update(self, *args):
        self.move()
        self.anim()

    def move(self):
        self.rect[0] -= 3

        if self.rect[0] <= -100:
            self.kill()

    def anim(self):                         # Animação das imagens.
        self.time = (self.time + 1) % 6
        self.image = pygame.image.load('Flappy_Image/' + str(self.time) + '.png')


class Dragon(Obj):
    def __init__(self, image, x, y, *groups):
        super().__init__(image, x, y, *groups)

        self.time = 0
        self.vel = 3
        self.grav = 1

        self.pts = 0

        self.play = True

    def update(self, *args):
        self.anim()
        self.move()

    def anim(self):
        self.time = (self.time + 1) % 4
        self.image = pygame.image.load('Flappy_Image/Dragon' + str(self.time) + '.png')

    def move(self):
        tecla = pygame.key.get_pressed()

        self.vel += self.grav               # Adição da gravidade.
        self.rect[1] += self.vel

        if self.vel >= 10:                  # Controle da velocidade.
            self.vel = 10

        if self.play:
            if tecla[pygame.K_SPACE]:           # Interação com o player.
                self.vel -= 4

        if self.rect[1] >= 650:             # Limite do chão e do teto.
            self.rect[1] = 650
        elif self.rect[1] <= 0:
            self.rect[1] = 0
            self.vel = 3

    def colision_pipes(self, group):        # Colisões e consequências.

        col = pygame.sprite.spritecollide(self, group, False)

        if col:
            self.play = False

    def colision_coin(self, group):

        col = pygame.sprite.spritecollide(self, group, True)

        if col:
            self.pts += 1

# Objeto para criar textos:

class Text:

    def __init__(self, size, text):
        self.init = pygame.font.init()
        self.font = pygame.font.Font('Flappy_Image/font/font.ttf', size)
        self.render = self.font.render(text, True, (255, 255, 255))

    def draw(self, window, x, y):
        window.blit(self.render, (x, y))

    def text_update(self, text):
        self.render = self.font.render(text, True, (255, 255, 255))