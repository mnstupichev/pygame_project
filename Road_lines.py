from load_image import load_image
import pygame

WIDTH = 600
HEIGHT = 480

WHITE = (255, 255, 255)
road_line_img = load_image("road_line.png", -1)

class Road_line(pygame.sprite.Sprite):
    def __init__(self, aboba, all_sprites, road_group, x):
        super().__init__(all_sprites)
        self.add(road_group)
        self.image = road_line_img
        self.rect = self.image.get_rect()
        self.speedx = -8 - aboba
        if self.speedx > 15:
            self.speedx = 15
        self.rect.bottom = HEIGHT - 30
        self.rect.right = x


    def update(self):
        self.rect.x += self.speedx
        if self.rect.right < 0:
            self.kill()
