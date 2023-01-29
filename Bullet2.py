from load_image import load_image
import pygame


bullet_img = load_image("bullet1.png", -1)
bullet_img = pygame.transform.scale(bullet_img, (20, 20))

class Bullet_of_second_player(pygame.sprite.Sprite):
    def __init__(self, x, y, speedy_of_bullet):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.right = y
        self.rect.centery = x
        self.speedy_of_bullet = speedy_of_bullet

    def update(self):
        self.rect.x -= self.speedy_of_bullet
        if self.rect.left < 0:
            self.kill()
