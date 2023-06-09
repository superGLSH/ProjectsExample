import os
import sys
import pygame
import random
import time

pygame.init()
pygame.key.set_repeat(200, 70)

FPS = 100
WIDTH = 512
HEIGHT = 512
STEP = 8

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = None
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
chel_group = pygame.sprite.Group()  # new

running = False
back_menu = False
tochno_back_menu = False
a = open("data/config.txt", "r")
uprav = a.readlines()[0]
a.close()

pygame.display.set_caption('SkySale')
pygame.display.set_icon(pygame.image.load("data/icon.png"))


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    max_width = max(map(len, level_map))

    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


def load_music(name, k):
    fullname = os.path.join('data', name)
    try:
        music = pygame.mixer.Sound(fullname)
        music.set_volume(k)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    return music


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '@':
                Tile('back', x, y)
                new_player = Player(x, y)
            elif level[y][x] == 'C':
                n = random.randint(0, 50)
                if n == 0 or n == 1:
                    Tile('back', x, y)
                    new_chel = Chel(x, y)
                elif 2 <= n <= 30:
                    Tile('grass', x, y)
                else:
                    Tile('back', x, y)
    return new_player, x, y


def terminate():
    b = open("data/config.txt", "w")
    b.write(uprav)
    b.close()
    pygame.quit()
    sys.exit()


def start_screen():
    global running

    intro_text = ["SkySale",
                  "",
                  "Вы - создатель Скайрима.",
                  "Продайте его."]
    fon = pygame.transform.scale(load_image('main.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    pygame.draw.rect(screen, pygame.Color("black"), (10, 200, 250, 100), 5)
    string_rendered = font.render('СТАРТ', 1, pygame.Color('black'))
    screen.blit(string_rendered, (100, 240))
    pygame.draw.rect(screen, pygame.Color("black"), (10, 350, 250, 100), 5)
    string_rendered = font.render('ВЫХОД', 1, pygame.Color('black'))
    screen.blit(string_rendered, (95, 390))

    while not running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 10 <= x <= 260 and 200 <= y <= 300:
                    running = True
                    game()
                elif 10 <= x <= 260 and 350 <= y <= 450:
                    terminate()
        pygame.display.flip()
        clock.tick(FPS)


tile_images = {'grass': load_image('grass.png'), 'back': load_image('back.png'), 'chell': load_image('chel_L.png'),
               'chelr': load_image('chel_R.png')}
quest = load_music("quest.mp3", 0.1)
music = load_music("music.mp3", 0.05)
player_image = load_image('gg64_L.png', -1)
tile_width = tile_height = 64
color1, color2 = pygame.Color('red'), pygame.Color('black')


def color_button():
    global uprav, color1, color2
    if uprav == "WASD":
        color1, color2 = pygame.Color('red'), pygame.Color('black')
    else:
        color1, color2 = color2, color1


color_button()


def option_menu():
    global uprav, color1, color2
    flag = True
    font = pygame.font.Font(None, 30)
    fon = pygame.transform.scale(load_image('main.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))

    pygame.draw.rect(screen, color1, (10, 50, 250, 100), 5)
    string_rendered = font.render('WASD-раскладка', 1, pygame.Color('black'))
    screen.blit(string_rendered, (55, 90))
    pygame.draw.rect(screen, color2, (10, 200, 250, 100), 5)
    string_rendered = font.render('Стрелочки', 1, pygame.Color('black'))
    screen.blit(string_rendered, (70, 240))
    pygame.draw.rect(screen, pygame.Color('black'), (10, 350, 250, 100), 5)
    string_rendered = font.render('НАЗАД', 1, pygame.Color('black'))
    screen.blit(string_rendered, (95, 390))

    while flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    flag = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 10 <= x <= 260 and 50 <= y <= 150:
                    if uprav != "WASD":
                        uprav = "WASD"
                        color_button()
                elif 10 <= x <= 260 and 200 <= y <= 300:
                    if uprav != "not WASD":
                        uprav = "not WASD"
                        color_button()
                elif 10 <= x <= 260 and 350 <= y <= 450:
                    flag = False
        pygame.display.flip()
        clock.tick(FPS)
        pygame.draw.rect(screen, color1, (10, 50, 250, 100), 5)
        pygame.draw.rect(screen, color2, (10, 200, 250, 100), 5)
    pause_menu()


def pause_menu():
    global running, back_menu, tochno_back_menu

    running = False
    font = pygame.font.Font(None, 30)
    fon = pygame.transform.scale(load_image('main.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))

    pygame.draw.rect(screen, pygame.Color("black"), (10, 50, 250, 100), 5)
    string_rendered = font.render('ПРОДОЛЖЕНИЕ', 1, pygame.Color('black'))
    screen.blit(string_rendered, (55, 90))
    pygame.draw.rect(screen, pygame.Color("black"), (10, 200, 250, 100), 5)
    string_rendered = font.render('НАСТРОЙКИ', 1, pygame.Color('black'))
    screen.blit(string_rendered, (70, 240))
    pygame.draw.rect(screen, pygame.Color("black"), (10, 350, 250, 100), 5)
    string_rendered = font.render('В ГЛАВНОЕ МЕНЮ', 1, pygame.Color('black'))
    screen.blit(string_rendered, (40, 390))

    while not running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 10 <= x <= 260 and 50 <= y <= 150:
                    running = True
                elif 10 <= x <= 260 and 200 <= y <= 300:
                    option_menu()
                elif 10 <= x <= 260 and 350 <= y <= 450:
                    running = True
                    back_menu = True
                    tochno_back_menu = True
        pygame.display.flip()
        clock.tick(FPS)


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


class Chel(pygame.sprite.Sprite):  # new
    def __init__(self, pos_x, pos_y):
        super().__init__(chel_group, all_sprites)
        self.frames = [tile_images['chell'], tile_images['chelr']]
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


class Camera:
    def __init__(self, field_size):
        self.dx = 0
        self.dy = 0
        self.field_size = field_size

    def apply(self, obj):
        obj.rect.x += self.dx
        if obj.rect.x < -obj.rect.width:
            obj.rect.x += (self.field_size[0] + 1) * obj.rect.width
        if obj.rect.x >= (self.field_size[0]) * obj.rect.width:
            obj.rect.x += -obj.rect.width * (1 + self.field_size[0])
        obj.rect.y += self.dy
        if obj.rect.y < -obj.rect.height:
            obj.rect.y += (self.field_size[1] + 1) * obj.rect.height
        if obj.rect.y >= (self.field_size[1]) * obj.rect.height:
            obj.rect.y += -obj.rect.height * (1 + self.field_size[1])

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - WIDTH // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - HEIGHT // 2)


def end(k):
    global running
    flagend = False

    fon = pygame.transform.scale(load_image('main.jpg'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    string_rendered = font.render('В ЭТОМ ГОДУ ВЫ ПРОДАЛИ', 1, pygame.Color('black'))
    screen.blit(string_rendered, (10, 10))
    string_rendered = font.render(str(k) + " ТЫС. КОПИЙ СКАЙРИМА", 1, pygame.Color('black'))
    screen.blit(string_rendered, (10, 50))

    pygame.draw.rect(screen, pygame.Color("black"), (10, 200, 250, 100), 5)
    string_rendered = font.render('ЗАНОВО', 1, pygame.Color('black'))
    screen.blit(string_rendered, (90, 240))
    pygame.draw.rect(screen, pygame.Color("black"), (10, 350, 250, 100), 5)
    string_rendered = font.render('В ГЛАВНОЕ МЕНЮ', 1, pygame.Color('black'))
    screen.blit(string_rendered, (40, 390))

    while not flagend:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 10 <= x <= 260 and 200 <= y <= 300:
                    running = True
                    game()
                elif 10 <= x <= 260 and 350 <= y <= 450:
                    flagend = True
        pygame.display.flip()
        clock.tick(FPS)


def game():
    global running, back_menu, tochno_back_menu
    music.play()
    timer = time.time()
    font = pygame.font.Font(None, 30)
    t = 12
    number = 0
    player, level_x, level_y = generate_level(load_level('map.txt'))
    camera = Camera((level_x, level_y))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    t = t - round(time.time() - timer)
                    pause_menu()
                    timer = time.time()
                if uprav == 'WASD':
                    if event.key == pygame.K_a:
                        player.image = load_image('gg64_L.png', -1)
                        player.rect.x -= STEP
                    if event.key == pygame.K_d:
                        player.image = load_image('gg64_R.png', -1)
                        player.rect.x += STEP
                    if event.key == pygame.K_w:
                        player.rect.y -= STEP
                    if event.key == pygame.K_s:
                        player.rect.y += STEP
                elif uprav == 'not WASD':
                    if event.key == pygame.K_LEFT:
                        player.image = load_image('gg64_L.png', -1)
                        player.rect.x -= STEP
                    if event.key == pygame.K_RIGHT:
                        player.image = load_image('gg64_R.png', -1)
                        player.rect.x += STEP
                    if event.key == pygame.K_UP:
                        player.rect.y -= STEP
                    if event.key == pygame.K_DOWN:
                        player.rect.y += STEP

        camera.update(player)

        for sprite in all_sprites:
            camera.apply(sprite)
        for i in chel_group:
            povtor = random.randint(0, 100)
            if povtor == 0:
                i.update()
            if abs(player.rect.x - i.rect.x) < 33 and abs(player.rect.y - i.rect.y) < 33:
                i.kill()
                t += 1
                quest.play()
                number += 1
        screen.fill(pygame.Color(0, 0, 0))
        tiles_group.draw(screen)
        chel_group.draw(screen)
        player_group.draw(screen)

        smesh = str(t - round(time.time() - timer))
        string_rendered = font.render(smesh, 1, pygame.Color('black'))
        screen.blit(string_rendered, (241 + 9 * (-len(smesh) + 2), 200))

        pygame.display.flip()
        clock.tick(FPS)

        if time.time() - timer > t:
            back_menu = True

        if back_menu == True:
            music.stop()
            running = False
            back_menu = False
            all_sprites.empty()
            tiles_group.empty()
            chel_group.empty()  # new
            player_group.empty()
            if not tochno_back_menu:
                end(number)
            tochno_back_menu = False
            start_screen()


start_screen()
terminate()
