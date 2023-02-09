import pygame
import random
from os import path
import csv

WIDTH = 600
HEIGHT = 480
FPS = 60

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

snd_dir = path.join(path.dirname(__file__), 'snd')

from Road_lines import Road_line
from Ball import Ball
from Block import Block
from Dino import Dino
from Platform1 import Platform1
from Platform2 import Platform2
from Player1 import Player1
from Player2 import Player2
from draw_lives import draw_lives
from load_image import load_image
from draw_text import draw_text
from go_to_winner_screen import go_to_winner_screen
from lobby import lobby

font_name = pygame.font.match_font('arial')
clock = pygame.time.Clock()

best_score_in_game = 0

with open ("data.csv", encoding="utf8") as database:
    data = csv.reader(database, delimiter=';', quotechar='"')
    for best_scores in data:
        best_score_in_game = int(best_scores[0])
database.close()

background = load_image("fon_lobby.png")
background = pygame.transform.scale(background, (600, 480))
background_rect = background.get_rect()

aboba = 0

#музыка
music = []
song = pygame.mixer.Sound(path.join(snd_dir, 'never.mp3'))
music.append(song)
for i in range(1, 8):
    song = pygame.mixer.Sound(path.join(snd_dir, f'{i}.mp3'))
    music.append(song)
rm = random.randrange(1, 8)
song = music[rm]

#Инициализация спарйтов
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player1 = Player1(all_sprites, bullets)
player2 = Player2(all_sprites, bullets)
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
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
            cort = lobby(game1, game2, game3, first_player_points, second_player_points, best_score_in_game, song, music, screen)
            game1 = cort[0]
            game2 = cort[1]
            game3 = cort[2]
            first_player_points = cort[3]
            second_player_points = cort[4]
            best_score = cort[5]
            song = cort[6]
            this_is_first_game = False
        else:
            cort = go_to_winner_screen(winner, first_player_points, second_player_points, screen)
            first_player_points = cort[0]
            second_player_points = cort[1]
            cort = lobby(game1, game2, game3, first_player_points, second_player_points, best_score_in_game, song, music, screen)
            game1 = cort[0]
            game2 = cort[1]
            game3 = cort[2]
            first_player_points = cort[3]
            second_player_points = cort[4]
            best_score = cort[5]
            song = cort[6]
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
                if best_score_in_game < best_score:
                    with open('data.csv', 'w', newline='', encoding="utf8") as database:
                        writer = csv.writer(
                            database, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                        writer.writerow([best_score])
                    database.close()
                    best_score_in_game = best_score

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