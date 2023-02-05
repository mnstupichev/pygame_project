import random

from Eyes import Eye
from load_image import load_image
import pygame

WIDTH = 600
HEIGHT = 480

WHITE = (255, 255, 255)

ball_img = load_image("ball.png", WHITE)

class Ball(pygame.sprite.Sprite):
    def __init__(self, platform1_group, platform2_group, all_sprites):
        self.platform1_group = platform1_group
        self.platform2_group = platform2_group
        pygame.sprite.Sprite.__init__(self)
        self.all_sprites = all_sprites
        self.image = ball_img
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = WIDTH / 2, HEIGHT / 2
        self.vx = random.randint(-4, 4)
        self.vy = random.randint(-4, 4)
        self.shoot_delay = 1000
        self.last_shot = pygame.time.get_ticks()
        self.speed_up_of_ball = 0

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.vx < 0:
                self.vx -= self.speed_up_of_ball
            else:
                self.vx += self.speed_up_of_ball
            if self.vy < 0:
                self.vy -= self.speed_up_of_ball
            else:
                self.vy += self.speed_up_of_ball

        self.rect = self.rect.move(self.vx, self.vy)

        rand = random.randrange(-1, 1)
        if self.rect.bottom > HEIGHT or self.rect.top < 0:
            self.vy = -self.vy
            self.vx += rand
        if pygame.sprite.spritecollideany(self, self.platform1_group):
            self.vx = -self.vx + rand
        if pygame.sprite.spritecollideany(self, self.platform2_group):
            self.vx = -self.vx + rand

        left_eye = Eye("left", self.rect.x, self.rect.y)
        right_eye = Eye("right", self.rect.x, self.rect.y)
        self.all_sprites.add(left_eye)
        self.all_sprites.add(right_eye)

