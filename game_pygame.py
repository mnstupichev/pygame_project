import pygame
import random
from os import path

from draw_lives import draw_lives
# from go_to_winner_screen import go_to_winner_screen
from load_image import load_image
# from show_go_screen import show_go_screen
from draw_text import draw_text

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
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')
snd_dir = path.join(path.dirname(__file__), 'snd')

player_img = load_image("pers.png", WHITE)
bullet_img = load_image("bullet1.png", -1)
platform_img = load_image("platform.png", WHITE)
ball_img = load_image("ball.png", WHITE)
bullet_img = pygame.transform.scale(bullet_img, (20, 20))
barrier_img = load_image("barrier.png", WHITE)
barrier_img = pygame.transform.scale(barrier_img, (40, 70))

class Player1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (40, 70))
        self.rect = self.image.get_rect()
        self.radius = 20
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centery = HEIGHT / 2
        self.rect.left = WIDTH - 570
        self.speedy = 0
        self.power = 1
        self.shoot_delay = 750
        self.last_shot = pygame.time.get_ticks()
        self.lives = 3
        self.speedy_of_bullet = 5


    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.speedy -= 8
        if keystate[pygame.K_s]:
            self.speedy += 8
        if keystate[pygame.K_d]:
            self.shoot()
        self.rect.y += self.speedy
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet_of_first_player(self.rect.centery, self.rect.right, self.speedy_of_bullet)
            all_sprites.add(bullet)
            bullets.add(bullet)


class Player2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (40, 70))
        self.image = pygame.transform.rotate(self.image, 180)
        self.image = pygame.transform.flip(self.image, False, True)
        self.rect = self.image.get_rect()
        self.radius = 20
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centery = HEIGHT / 2
        self.rect.right = WIDTH - 30
        self.speedy = 0
        self.power = 1
        self.shoot_delay = 750
        self.last_shot = pygame.time.get_ticks()
        self.lives = 3
        self.speedy_of_bullet = 5

    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_o]:
            self.speedy -= 8
        if keystate[pygame.K_l]:
            self.speedy += 8
        if keystate[pygame.K_k]:
            self.shoot()
        self.rect.y += self.speedy
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet_of_second_player(self.rect.centery, self.rect.left, self.speedy_of_bullet)
            all_sprites.add(bullet)
            bullets.add(bullet)


class Bullet_of_first_player(pygame.sprite.Sprite):
    def __init__(self, x, y, speedy_of_bullet):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.left = y
        self.rect.centery = x
        self.speedy_of_bullet = speedy_of_bullet

    def update(self):
        self.rect.x += self.speedy_of_bullet
        if self.rect.right > WIDTH:
            self.kill()

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

class Ball(pygame.sprite.Sprite):
    def __init__(self):
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

        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = -self.vx
        if pygame.sprite.spritecollideany(self, platform1_group):
            self.vx = -self.vx
        if pygame.sprite.spritecollideany(self, platform2_group):
            self.vx = -self.vx


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        self.add(horizontal_borders)
        self.image = pygame.Surface([x2 - x1, 5])
        self.image.fill(WHITE)
        self.rect = pygame.Rect(x1, y1, x2 - x1, y2)

class Platform1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.add(platform1_group)
        self.image = platform_img
        self.image = pygame.transform.scale(platform_img, (60, 20))
        self.image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()
        self.rect.centery = HEIGHT / 2
        self.rect.left = WIDTH - 570
        self.speedy = 0
        self.lives = 3


    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.speedy -= 12
        if keystate[pygame.K_s]:
            self.speedy += 12
        self.rect.y += self.speedy
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class Platform2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.add(platform1_group)
        self.image = platform_img
        self.image = pygame.transform.scale(platform_img, (60, 20))
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.centery = HEIGHT / 2
        self.rect.left = WIDTH - 30
        self.speedy = 0
        self.lives = 3


    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_o]:
            self.speedy -= 12
        if keystate[pygame.K_l]:
            self.speedy += 12
        self.rect.y += self.speedy
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT


class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.sheet = load_image("dino.png", (64, 202, 201))
        self.add(dino_group)
        self.frames = []
        self.cut_sheet(self.sheet, 5, 1)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHT - 30
        self.rect.left = WIDTH - 530
        self.speedy = 0

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                for k in range(10):
                    self.frames.append(sheet.subsurface(pygame.Rect(
                        frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        self.mask = pygame.mask.from_surface(self.image)
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE] and self.rect.bottom == HEIGHT - 30:
            self.speedy = -15
        self.rect.y += self.speedy
        if self.rect.y < HEIGHT - 320:
            self.rect.y = HEIGHT - 320
            self.speedy = 12
        if self.rect.bottom > HEIGHT - 30:
            self.speedy = 0
            self.rect.bottom = HEIGHT - 30

class Block(pygame.sprite.Sprite):
    def __init__(self, num, aboba):
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


screen_rect = (0, 0, WIDTH, HEIGHT)

class Particle(pygame.sprite.Sprite):
    # сгенерируем частицы разного размер

    def __init__(self, pos, dx, dy):
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
        if not self.rect.colliderect(screen_rect):
            self.kill()

class Arrow(pygame.sprite.Sprite):
    image = load_image("arrow_mouse.png")

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Arrow.image
        self.rect = self.image.get_rect()
        if pygame.mouse.get_focused():
            self.rect.x = pygame.mouse.get_pos()[0]
            self.rect.y = pygame.mouse.get_pos()[1]

    def update(self):
        self.rect.x = pygame.mouse.get_pos()[0]
        self.rect.y = pygame.mouse.get_pos()[1]

def show_go_screen():
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
    background = load_image("grid_bg.png")
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
    waiting = True
    while waiting:
        pygame.mouse.set_visible(False)
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEMOTION:
                screen.fill((0, 0, 0))
                screen.blit(background, background_rect)
                draw_text(screen, f"First player points: {first_player_points}", 20, 80, 20)
                draw_text(screen, f"Second player points: {second_player_points}", 20, WIDTH - 100, 20)
                draw_text(screen, f"Best score in game 3: {best_score}", 20, WIDTH / 2, HEIGHT - 50)
                draw_text(screen, "Choose one game!", 50, WIDTH / 2, HEIGHT / 4 - 50)
                draw_text(screen, "Game 1", 50, WIDTH / 2, HEIGHT - 300)
                draw_text(screen, "Game 2", 50, WIDTH / 2, HEIGHT - 210)
                draw_text(screen, "Game 3", 50, WIDTH / 2, HEIGHT - 120)
                arrow = Arrow()
                all_sprites.add(arrow)
                all_sprites.update()
                all_sprites.draw(screen)

            if event.type == pygame.MOUSEBUTTONDOWN and \
                    WIDTH / 2 + 60 > event.pos[0] > WIDTH / 2 - 60 and \
                    230 > event.pos[1] > 180:
                game1 = True
                game2 = False
                game3 = False
                waiting = False

            if event.type == pygame.MOUSEBUTTONDOWN and \
                    WIDTH / 2 + 60 > event.pos[0] > WIDTH / 2 - 60 and \
                    320 > event.pos[1] > 270:
                game1 = False
                game2 = True
                game3 = False
                waiting = False

            if event.type == pygame.MOUSEBUTTONDOWN and \
                    WIDTH / 2 + 60 > event.pos[0] > WIDTH / 2 - 60 and \
                    410 > event.pos[1] > 360:
                game1 = False
                game2 = False
                game3 = True
                waiting = False
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
    if winner == "FIRST_PLAYER":
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
                show_go_screen()
                waiting = False
        now = pygame.time.get_ticks()
        if now - one_s > 100:
            one_s = now
            x = random.randrange(1, 599)
            y = random.randrange(1, 479)
            particle_count = 20
            # возможные скорости
            numbers = range(-5, 6)
            for _ in range(particle_count):
                particle = Particle((x, y), random.choice(numbers), random.choice(numbers))
                all_sprites.add(particle)

        all_sprites.update()
        screen.fill((0, 0, 0))
        screen.blit(background_of_winner_screen, background_of_winner_screen_rect)
        draw_text(screen, f"{winner} WON!", 50, WIDTH / 2, HEIGHT - 100)
        all_sprites.draw(screen)
        pygame.display.flip()


background = load_image("grid_bg.png")
background = pygame.transform.scale(background, (600, 480))
background_rect = background.get_rect()

aboba = 0

all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player1 = Player1()
player2 = Player2()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
border1 = Border(0, 5, WIDTH, 5)
border2 = Border(0, HEIGHT - 5, WIDTH, HEIGHT - 5)
ball = Ball()
platform1_group = pygame.sprite.Group()
platform2_group = pygame.sprite.Group()
platform1 = Platform1()
platform2 = Platform2()
dino_group = pygame.sprite.Group()
dino = Dino()
block_group = pygame.sprite.Group()
block = Block(0, aboba)
hp = load_image("heart.png", WHITE)
hp = pygame.transform.scale(hp, (50, 50))



pygame.time.set_timer(pygame.USEREVENT, 1000)

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

last_spaun = 0
one_s =0
counter = 0

game_over = True
running = True
winner = ''
this_is_first_game = True

while running:
    pygame.mouse.set_visible(False)
    if game_over:
        if this_is_first_game or game3_flag:
            game3_flag = False
            show_go_screen()
            this_is_first_game = False
        else:
            go_to_winner_screen(winner)
        speedy_of_bullet = 5
        if game1:
            all_sprites = pygame.sprite.Group()
            bullets = pygame.sprite.Group()
            player1 = Player1()
            player2 = Player2()
            all_sprites.add(player1)
            all_sprites.add(player2)
            background = load_image("fon_for_first_game.png")
            background = pygame.transform.scale(background, (600, 480))
            background_rect = background.get_rect()
        if game2:
            all_sprites = pygame.sprite.Group()
            ball = Ball()
            border1 = Border(5, 5, WIDTH - 5, 5)
            border2 = Border(5, HEIGHT - 5, WIDTH - 5, HEIGHT - 5)
            platform1 = Platform1()
            platform2 = Platform2()
            all_sprites.add(ball)
            all_sprites.add(platform1)
            all_sprites.add(platform2)
            all_sprites.add(border1)
            all_sprites.add(border2)
            background = load_image("fon_for_second_game.png")
            background = pygame.transform.scale(background, (600, 480))
            background_rect = background.get_rect()
        if game3:
            all_sprites = pygame.sprite.Group()
            dino = Dino()
            block = Block(-1, aboba)
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
            winner = "SECOND_PLAYER"
            game_over = True

        if player2.lives == 0:
            winner = "FIRST_PLAYER"
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
            ball = Ball()
            all_sprites.add(ball)
            ball.speed_up_of_bullet = 3

        if ball.rect.left > WIDTH:
            platform2.lives -= 1
            ball.kill()
            ball = Ball()
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
        draw_lives(screen, 20, 5, platform1.lives,
                   hp)
        draw_lives(screen, WIDTH - 120, 5, platform2.lives,
                   hp)
        all_sprites.draw(screen)
        pygame.display.flip()

    if game3:
        all_sprites.update()
        now = pygame.time.get_ticks()
        time_of_next_block = random.randrange(1000, 3000)
        num_of_blocks = random.randrange(1, 4)
        if now - last_spaun > time_of_next_block:
            last_spaun = now
            aboba += 1
            for i in range(num_of_blocks):
                block = Block(i, aboba)
                all_sprites.add(block)

        hits = pygame.sprite.spritecollide(dino, block_group, True)
        for hit in hits:
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