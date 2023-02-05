from load_image import load_image
import pygame

WIDTH = 600
HEIGHT = 480

class Dino(pygame.sprite.Sprite):
    def __init__(self, all_sprites, dino_group):
        super().__init__(all_sprites)
        self.sheet = load_image("dino.png", -1)
        #(64, 202, 201)
        self.add(dino_group)
        self.frames = []
        self.cut_sheet(self.sheet, 4, 1)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT - 40
        self.rect.left = WIDTH - 530
        self.speedy = 0

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                for k in range(10):
                    self.frames.append(sheet.subsurface(pygame.Rect(
                        frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        self.mask = pygame.mask.from_surface(self.image)
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE] and self.rect.bottom == HEIGHT - 40:
            self.speedy = -15
        self.rect.y += self.speedy
        if self.rect.y < HEIGHT - 330:
            self.rect.y = HEIGHT - 330
            self.speedy = 12
        if self.rect.bottom > HEIGHT - 40:
            self.speedy = 0
            self.rect.bottom = HEIGHT - 40
