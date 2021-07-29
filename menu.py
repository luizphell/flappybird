from  obj import Obj, Text
import pygame

class Menu:

    def __init__(self):             # Adicionar sprites do menu.
        self.all_sprites = pygame.sprite.Group()

        self.field = Obj('Flappy_Image/landscape-1769052_1280.png', 0, 0, self.all_sprites)
        self.field2 = Obj('Flappy_Image/landscape-1769052_1280.png', 1280, 0, self.all_sprites)

        self.get_ready = Obj('Flappy_Image/getready.png', 530, 70, self.all_sprites)
        self.table_score = Obj('Flappy_Image/score.png', 493, 230, self.all_sprites)
        self.go_play = Obj('Flappy_Image/go.png', 565, 500, self.all_sprites)

        self.change_scene = False

        self.text_score = Text(100, '0')

    def draw(self, window):
        self.all_sprites.draw(window)
        self.text_score.draw(window, 635, 300)

    def update(self, pts):
        self.all_sprites.update()
        self.move_field()
        self.text_score.text_update(pts)

    def events(self, event):                    # Interação com o player.
        if event.type == pygame.MOUSEBUTTONUP:
            if self.go_play.rect.collidepoint(pygame.mouse.get_pos()):
                self.change_scene = True
                print('mouse')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.change_scene = True
                print('teclado')


    def move_field(self):
        self.field.rect[0] -= 3
        self.field2.rect[0] -= 3

        if self.field.rect[0] <= -1280:
            self.field.rect[0] = 0
        if self.field2.rect[0] <= 0:
            self.field2.rect[0] = 1280