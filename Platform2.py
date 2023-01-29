from load_image import load_image
import pygame

WIDTH = 600
HEIGHT = 480

WHITE = (255, 255, 255)

platform_img = load_image("platform.png", WHITE)


class Platform2(pygame.sprite.Sprite):
    def __init__(self, all_sprites, platform2_group):
        super().__init__(all_sprites)
        self.add(platform2_group)
        self.image = platform_img
        self.image = pygame.transform.scale(platform_img, (60, 20))
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.centery = HEIGHT / 2
        self.rect.left = WIDTH - 30
        self.speedy = 0
        self.lives = 3


    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_o]:
            self.speedy -= 12
        if keystate[pygame.K_l]:
            self.speedy += 12
        self.rect.y += self.speedy
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
