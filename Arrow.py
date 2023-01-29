from load_image import load_image
import pygame

class Arrow(pygame.sprite.Sprite):
    image = load_image("arrow_mouse.png")

    def __init__(self, all_sprites):
        super().__init__(all_sprites)
        self.image = Arrow.image
        self.rect = self.image.get_rect()
        if pygame.mouse.get_focused():
            self.rect.x = pygame.mouse.get_pos()[0]
            self.rect.y = pygame.mouse.get_pos()[1]

    def update(self):
        self.rect.x = pygame.mouse.get_pos()[0]
        self.rect.y = pygame.mouse.get_pos()[1]
