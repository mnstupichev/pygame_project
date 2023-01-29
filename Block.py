from load_image import load_image
import pygame

WIDTH = 600
HEIGHT = 480

WHITE = (255, 255, 255)
barrier_img = load_image("barrier.png", WHITE)
barrier_img = pygame.transform.scale(barrier_img, (40, 70))

class Block(pygame.sprite.Sprite):
    def __init__(self, num, aboba, all_sprites, block_group):
        super().__init__(all_sprites)
        self.add(block_group)
        self.image = barrier_img
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.speedx = -8 - aboba
        if self.speedx > 20:
            self.speedx = 20
        if num == -1:
            self.rect.bottom = HEIGHT + 100
            self.rect.right = WIDTH
        else:
            self.rect.bottom = HEIGHT - 30
            self.rect.right = WIDTH + 20 * num


    def update(self):
        self.rect.x += self.speedx
        if self.rect.right < 0:
            self.kill()
