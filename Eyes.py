from load_image import load_image
import pygame

WIDTH = 600
HEIGHT = 480

WHITE = (255, 255, 255)
eye_img = load_image("eye.png", -1)

class Eye(pygame.sprite.Sprite):
    def __init__(self, which, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = eye_img
        self.rect = self.image.get_rect()
        if which == "left":
            self.rect.x = WIDTH - 365 + x / 50
            self.rect.y = HEIGHT - 300 + y / 50
        else:
            self.rect.x = WIDTH - 290 + x / 50
            self.rect.y = HEIGHT - 300 + y / 50

    def update(self):
        self.kill()
