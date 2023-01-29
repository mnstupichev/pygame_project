import random

from load_image import load_image
import pygame

WIDTH = 600
HEIGHT = 480

WHITE = (255, 255, 255)

ball_img = load_image("ball.png", WHITE)

class Ball(pygame.sprite.Sprite):
    def __init__(self, horizontal_borders, platform1_group, platform2_group):
        self.horizontal_borders = horizontal_borders
        self.platform1_group = platform1_group
        self.platform2_group = platform2_group
        pygame.sprite.Sprite.__init__(self)
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

        if pygame.sprite.spritecollideany(self, self.horizontal_borders):
            self.vy = -self.vx
        if pygame.sprite.spritecollideany(self, self.platform1_group):
            self.vx = -self.vx
        if pygame.sprite.spritecollideany(self, self.platform2_group):
            self.vx = -self.vx
