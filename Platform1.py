from load_image import load_image
import pygame

WIDTH = 600
HEIGHT = 480

WHITE = (255, 255, 255)

platform_img = load_image("platform.png", WHITE)

class Platform1(pygame.sprite.Sprite):
    def __init__(self, all_sprites, platform1_group):
        super().__init__(all_sprites)
        self.add(platform1_group)
        self.image = platform_img
        self.image = pygame.transform.scale(platform_img, (60, 20))
        self.image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()
        self.rect.centery = HEIGHT / 2
        self.rect.left = WIDTH - 570
        self.speedy = 0
        self.lives = 3


    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.speedy -= 12
        if keystate[pygame.K_s]:
            self.speedy += 12
        self.rect.y += self.speedy
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
