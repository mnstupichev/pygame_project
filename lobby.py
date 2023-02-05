import random
import pygame

from Player_in_lobby import Player
from draw_text import draw_text
from load_image import load_image


WIDTH = 600
HEIGHT = 480
FPS = 60
clock = pygame.time.Clock()

def lobby(game1, game2, game3, first_player_points, second_player_points, best_score, song, music, screen):
    song.stop()
    rm = random.randrange(0, 8)
    song = music[rm]
    song.play()
    background = load_image("fon_lobby.png")
    background = pygame.transform.scale(background, (600, 480))
    background_rect = background.get_rect()
    screen.blit(background, background_rect)
    draw_text(screen, f"First player points: {first_player_points}", 20, 80, 20)
    draw_text(screen, f"Second player points: {second_player_points}", 20, WIDTH - 100, 20)
    draw_text(screen, f"Best score in game 3: {best_score}", 20, WIDTH / 2, HEIGHT - 50)
    draw_text(screen, "Choose one game!", 50, WIDTH / 2, HEIGHT / 4 - 50)
    draw_text(screen, "Game 1", 50, WIDTH / 2, HEIGHT - 300)
    draw_text(screen, "Game 2", 50, WIDTH / 2, HEIGHT - 210)
    draw_text(screen, "Game 3", 50, WIDTH / 2, HEIGHT - 120)
    pygame.display.flip()
    all_sprites = pygame.sprite.Group()
    player = Player(all_sprites)
    all_sprites.add(player)
    waiting = True
    while waiting:
        pygame.mouse.set_visible(False)
        clock.tick(FPS)
        keystate = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if keystate[pygame.K_SPACE] and \
                    WIDTH / 2 + 60 > player.rect.center[0] > WIDTH / 2 - 60 and \
                    230 > player.rect.center[1] > 180:
                game1 = True
                game2 = False
                game3 = False
                waiting = False

            if keystate[pygame.K_SPACE] and \
                    WIDTH / 2 + 60 > player.rect.center[0] > WIDTH / 2 - 60 and \
                    320 > player.rect.center[1] > 270:
                game1 = False
                game2 = True
                game3 = False
                waiting = False

            if keystate[pygame.K_SPACE] and \
                    WIDTH / 2 + 60 > player.rect.center[0] > WIDTH / 2 - 60 and \
                    410 > player.rect.center[1] > 360:
                game1 = False
                game2 = False
                game3 = True
                waiting = False

        screen.fill((0, 0, 0))
        screen.blit(background, background_rect)
        draw_text(screen, f"First player points: {first_player_points}", 20, 80, 20)
        draw_text(screen, f"Second player points: {second_player_points}", 20, WIDTH - 100, 20)
        draw_text(screen, f"Best score in game 3: {best_score}", 20, WIDTH / 2, HEIGHT - 50)
        draw_text(screen, "Choose one game!", 50, WIDTH / 2, HEIGHT / 4 - 50)
        draw_text(screen, "Game 1", 50, WIDTH / 2, HEIGHT - 300)
        draw_text(screen, "Game 2", 50, WIDTH / 2, HEIGHT - 210)
        draw_text(screen, "Game 3", 50, WIDTH / 2, HEIGHT - 120)
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()

    return (game1, game2, game3, first_player_points, second_player_points, best_score, song)
