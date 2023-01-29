from Bullet1 import Bullet_of_first_player
from load_image import load_image
import pygame

WIDTH = 600
HEIGHT = 480

WHITE = (255, 255, 255)
player_img = load_image("pers.png", WHITE)

class Player1(pygame.sprite.Sprite):
    def __init__(self, all_sprites, bullets):
        pygame.sprite.Sprite.__init__(self)
        self.all_sprites = all_sprites
        self.bullets = bullets
        self.image = pygame.transform.scale(player_img, (40, 70))
        self.rect = self.image.get_rect()
        self.radius = 20
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centery = HEIGHT / 2
        self.rect.left = WIDTH - 570
        self.speedy = 0
        self.power = 1
        self.shoot_delay = 750
        self.last_shot = pygame.time.get_ticks()
        self.lives = 3
        self.speedy_of_bullet = 5


    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.speedy -= 8
        if keystate[pygame.K_s]:
            self.speedy += 8
        if keystate[pygame.K_d]:
            self.shoot()
        self.rect.y += self.speedy
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet_of_first_player(self.rect.centery, self.rect.right, self.speedy_of_bullet)
            self.all_sprites.add(bullet)
            self.bullets.add(bullet)
