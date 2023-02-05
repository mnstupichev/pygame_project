import pygame
import random
from os import path

WIDTH = 600
HEIGHT = 480
FPS = 60
POWERUP_TIME = 5000

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("1000 и 1 баг")

from Road_lines import Road_line
from Ball import Ball
from Block import Block
from Border import Border
from Dino import Dino
from Particle import Particle
from Platform1 import Platform1
from Platform2 import Platform2
from Eyes import Eye
from Player1 import Player1
from Player2 import Player2
from Player_in_lobby import Player
from draw_lives import draw_lives
from load_image import load_image
from draw_text import draw_text

font_name = pygame.font.match_font('arial')
snd_dir = path.join(path.dirname(__file__), 'snd')
clock = pygame.time.Clock()


def lobby():
    global game1
    global game2
    global game3
    global first_player_points
    global second_player_points
    global best_score
    global song
    song.stop()
    rm = random.randrange(1, 8)
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


def go_to_winner_screen(winner):
    global first_player_points
    global second_player_points
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
                lobby()
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


background = load_image("fon_lobby.png")
background = pygame.transform.scale(background, (600, 480))
background_rect = background.get_rect()

aboba = 0

all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player1 = Player1(all_sprites, bullets)
player2 = Player2(all_sprites, bullets)
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
border1 = Border(0, 5, WIDTH, 5, all_sprites, horizontal_borders)
border2 = Border(0, HEIGHT - 5, WIDTH, HEIGHT - 5, all_sprites, horizontal_borders)
platform1_group = pygame.sprite.Group()
platform2_group = pygame.sprite.Group()
ball = Ball(platform1_group, platform2_group, all_sprites)
platform1 = Platform1(all_sprites, platform1_group)
platform2 = Platform2(all_sprites, platform2_group)
dino_group = pygame.sprite.Group()
dino = Dino(all_sprites, dino_group)
block_group = pygame.sprite.Group()
block = Block(0, aboba, all_sprites, block_group)
road_group = pygame.sprite.Group()
road_line = Road_line(aboba, all_sprites, road_group, -100)

hp = load_image("heart.png", WHITE)
hp = pygame.transform.scale(hp, (50, 50))

pygame.time.set_timer(pygame.USEREVENT, 1000)

# музыка
music = []
song = pygame.mixer.Sound(path.join(snd_dir, 'never.mp3'))
music.append(song)
for i in range(1, 8):
    song = pygame.mixer.Sound(path.join(snd_dir, f'{i}.mp3'))
    music.append(song)
rm = random.randrange(1, 8)
song = music[rm]

game1 = False
game2 = False
game3 = False
game3_flag = False

first_player_points = 0
second_player_points = 0
best_score = 0

last_spaun_block = 0
last_spaun_line = 0
one_s = 0
counter = 0

game_over = True
running = True
winner = ''
this_is_first_game = True

# основной цикл
while running:
    pygame.mouse.set_visible(False)
    if game_over:
        if this_is_first_game or game3_flag:
            game3_flag = False
            lobby()
            this_is_first_game = False
        else:
            go_to_winner_screen(winner)
        speedy_of_bullet = 5
        if game1:
            all_sprites = pygame.sprite.Group()
            bullets = pygame.sprite.Group()
            player1 = Player1(all_sprites, bullets)
            player2 = Player2(all_sprites, bullets)
            all_sprites.add(player1)
            all_sprites.add(player2)
            background = load_image("fon_for_first_game.png")
            background = pygame.transform.scale(background, (600, 480))
            background_rect = background.get_rect()
        if game2:
            all_sprites = pygame.sprite.Group()
            ball = Ball(platform1_group, platform2_group, all_sprites)
            platform1 = Platform1(all_sprites, platform1_group)
            platform2 = Platform2(all_sprites, platform2_group)
            all_sprites.add(ball)
            all_sprites.add(platform1)
            all_sprites.add(platform2)
            background = load_image("fon_for_second_game.png")
            background = pygame.transform.scale(background, (600, 480))
            background_rect = background.get_rect()
        if game3:
            all_sprites = pygame.sprite.Group()
            dino = Dino(all_sprites, dino_group)
            block_group = pygame.sprite.Group()
            block = Block(-1, aboba, all_sprites, block_group)
            road_group = pygame.sprite.Group()
            for i in range(100, 500, 200):
                road_line = Road_line(aboba, all_sprites, road_group, i)
                all_sprites.add(road_line)
            all_sprites.add(dino)
            all_sprites.add(block)
            background = load_image("fon_for_third_game.png")
            background = pygame.transform.scale(background, (600, 480))
            background_rect = background.get_rect()
            counter = 0
            last_spaun = 0
            aboba = 0

        game_over = False

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT:
            player1.speedy_of_bullet += 3
            player2.speedy_of_bullet += 3
        if event.type == pygame.USEREVENT:
            ball.speed_up_of_ball += 0.1

    if game1:
        all_sprites.update()

        hits = pygame.sprite.spritecollide(player1, bullets, True)
        for hit in hits:
            player1.lives -= 1

        hits = pygame.sprite.spritecollide(player2, bullets, True)
        for hit in hits:
            player2.lives -= 1

        if player1.lives == 0:
            winner = "SECOND PLAYER"
            game_over = True

        if player2.lives == 0:
            winner = "FIRST PLAYER"
            game_over = True

        screen.fill(BLACK)
        screen.blit(background, background_rect)
        draw_lives(screen, 20, 5, player1.lives, hp)
        draw_lives(screen, WIDTH - 120, 5, player2.lives, hp)
        all_sprites.draw(screen)
        pygame.display.flip()

    if game2:
        all_sprites.update()

        if ball.rect.right < 0:
            platform1.lives -= 1
            ball.kill()
            ball = Ball(platform1_group, platform2_group, all_sprites)
            all_sprites.add(ball)
            ball.speed_up_of_bullet = 3

        if ball.rect.left > WIDTH:
            platform2.lives -= 1
            ball.kill()
            ball = Ball(platform1_group, platform2_group, all_sprites)
            all_sprites.add(ball)
            ball.speed_up_of_bullet = 3

        if platform1.lives == 0:
            winner = "SECOND_PLAYER"
            game_over = True

        if platform2.lives == 0:
            winner = "FIRST_PLAYER"
            game_over = True

        screen.fill(BLACK)
        screen.blit(background, background_rect)
        draw_lives(screen, 20, 5, platform1.lives, hp)
        draw_lives(screen, WIDTH - 120, 5, platform2.lives, hp)
        all_sprites.draw(screen)
        pygame.display.flip()

    if game3:
        all_sprites.update()
        now = pygame.time.get_ticks()
        time_of_next_block = random.randrange(1000, 2500)
        num_of_blocks = random.randrange(1, 4)
        if now - last_spaun_block > time_of_next_block:
            last_spaun_block = now
            aboba += 1
            for i in range(num_of_blocks):
                block = Block(i, aboba, all_sprites, block_group)
                all_sprites.add(block)

        time_of_next_line = 300
        if now - last_spaun_line > time_of_next_line:
            last_spaun_line = now
            road_line = Road_line(aboba, all_sprites, road_group, WIDTH)
            all_sprites.add(road_line)


        for block in block_group:
            if pygame.sprite.collide_mask(dino, block):
                game3_flag = True
                game_over = True

        if best_score < counter:
            best_score = counter

        if now - one_s > 200:
            one_s = now
            counter += 1

        screen.fill(BLACK)
        screen.blit(background, background_rect)
        draw_text(screen, f"SCORE: {counter}", 40, WIDTH - 510, 20, BLUE)
        all_sprites.draw(screen)
        pygame.display.flip()

pygame.quit()
