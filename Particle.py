import random
import pygame

from load_image import load_image

WIDTH = 600
HEIGHT = 480

class Particle(pygame.sprite.Sprite):
    # сгенерируем частицы разного размер

    def __init__(self, pos, dx, dy, all_sprites):
        super().__init__(all_sprites)
        self.image = load_image("star.png")
        ri = random.randrange(5, 20)
        self.image = pygame.transform.scale(self.image, (ri, ri))
        self.rect = self.image.get_rect()

        # у каждой частицы своя скорость — это вектор
        self.velocity = [dx, dy]
        # и свои координаты
        self.rect.x, self.rect.y = pos

        # гравитация будет одинаковой (значение константы)
        self.gravity = 0.5

    def update(self):
        # применяем гравитационный эффект:
        # движение с ускорением под действием гравитации
        self.velocity[1] += self.gravity
        # перемещаем частицу
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        # убиваем, если частица ушла за экран
        screen_rect = (0, 0, WIDTH, HEIGHT)
        if not self.rect.colliderect(screen_rect):
            self.kill()
