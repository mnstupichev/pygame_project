import random
import pygame

from Particle import Particle
from draw_text import draw_text
from load_image import load_image

WIDTH = 600
HEIGHT = 480
FPS = 60


def go_to_winner_screen(winner, first_player_points, second_player_points, screen):
    background_of_winner_screen = load_image("winner_background.png")
    background_of_winner_screen = pygame.transform.scale(background_of_winner_screen, (600, 480))
    background_of_winner_screen_rect = background_of_winner_screen.get_rect()

    screen.blit(background_of_winner_screen, background_of_winner_screen_rect)
    draw_text(screen, f"{winner} WON!", 50, WIDTH / 2, HEIGHT - 100)
    pygame.display.flip()
    if winner == "FIRST PLAYER":
        first_player_points += 1
    else:
        second_player_points += 1
    waiting = True
    all_sprites = pygame.sprite.Group()
    clock = pygame.time.Clock()
    one_s = 0
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                waiting = False
        now = pygame.time.get_ticks()
        if now - one_s > 100:
            one_s = now
            x = random.randrange(1, 599)
            y = random.randrange(1, 479)
            particle_count = 20
            numbers = range(-5, 6)
            for _ in range(particle_count):
                particle = Particle((x, y), random.choice(numbers), random.choice(numbers), all_sprites)
                all_sprites.add(particle)

        all_sprites.update()
        screen.fill((0, 0, 0))
        screen.blit(background_of_winner_screen, background_of_winner_screen_rect)
        draw_text(screen, f"{winner} WON!", 50, WIDTH / 2, HEIGHT - 100)
        all_sprites.draw(screen)
        pygame.display.flip()

    return (first_player_points, second_player_points)
