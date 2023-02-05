import pygame
from load_image import load_image


WIDTH = 600
HEIGHT = 480

WHITE = (255, 255, 255)
player_img = load_image("pers.png", WHITE)

class Player(pygame.sprite.Sprite):
    def __init__(self, all_sprites):
        super().__init__(all_sprites)
        self.image = pygame.transform.scale(player_img, (40, 70))
        self.rect = self.image.get_rect()
        self.rect.y = 20
        self.rect.left = 20


    def update(self):
        self.speedy = 0
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.speedy -= 2
        if keystate[pygame.K_s]:
            self.speedy += 2
        self.rect.y += self.speedy
        if keystate[pygame.K_a]:
            self.image = pygame.transform.scale(player_img, (40, 70))
            self.image = pygame.transform.rotate(self.image, 180)
            self.image = pygame.transform.flip(self.image, False, True)
            self.speedx -= 2
        if keystate[pygame.K_d]:
            self.image = pygame.transform.scale(player_img, (40, 70))
            self.speedx += 2
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH