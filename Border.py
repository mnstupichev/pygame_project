import pygame

WHITE = (255, 255, 255)

class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2, all_sprites, horizontal_borders):
        super().__init__(all_sprites)
        self.add(horizontal_borders)
        self.image = pygame.Surface([x2 - x1, 5])
        self.image.fill(WHITE)
        self.rect = pygame.Rect(x1, y1, x2 - x1, y2)
