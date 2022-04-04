import pygame
from random import randrange

RES = 800
SIZE = 50
score = 0
lives = 3
fps = 20

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
surface = pygame.display.set_mode([800, 523])
clock = pygame.time.Clock()

font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_lives = pygame.font.SysFont('Arial', 26, bold=True)

fon_asteroid = pygame.image.load('fon_asteroids.png').convert()
img = pygame.image.load('1.png').convert()

big_asteroid = pygame.image.load('big_asteroid.png').convert()


ship_on_stay = pygame.image.load('ship_on_stay.png').convert()
ship_on_move = pygame.image.load('ship_on_move.png').convert()
angle = 0

fon_asteroid.set_colorkey((255, 255, 255))
ship_on_stay.set_colorkey((255, 255, 255))
ship_on_move.set_colorkey((255, 255, 255))
big_asteroid.set_colorkey((255, 255, 255))

# Создание фоновых астеройдов
aster_list = []

for i in range(25):
    aster_start_x = randrange(20, 1000)
    aster_start_y = randrange(0, 500)
    aster_list.append([aster_start_x, aster_start_y, randrange(1, 4)])

# Создание больших астеройдов

big_asrers = []
asters = []
for i in range(4):
    aster_start_x = randrange(80, 720)
    aster_start_y = randrange(80, 400)
    big_aster_angle = randrange(1, 4)

    big_asrers.append([aster_start_x, aster_start_y, big_aster_angle])
# Переменные для заставки
scale = True
size = 36
start = 220

# Переменные для вращения корабля
start_flag = False
rotate_right = False
rotate_left = False
move = False


while True:
    surface.blit(img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            start_flag = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rotate_right = True
            elif event.key == pygame.K_LEFT:
                rotate_left = True
            elif event.key == pygame.K_SPACE:
                move = True
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                rotate_right = rotate_left = False
            if event.key == pygame.K_SPACE:
                move = False

    for i in range(len(aster_list)):

        surface.blit(fon_asteroid, (aster_list[i][0], aster_list[i][1]))
        aster_list[i][0] -= aster_list[i][2]

        if aster_list[i][0] < -50:
            aster_list[i][0] = 840

    if not start_flag:
        # show start menu
        if scale:
            size += 1
            start -= 4
            if size == 40:
                scale = False
        else:
            size -= 1
            start += 4
            if size == 36:
                scale = True

        font_start_menu = pygame.font.SysFont('Arial', size, bold=True)
        render_start = font_start_menu.render(f'Нажми чтобы начать', True, pygame.Color('yellow'))
        surface.blit(render_start, (start, 251))

    else:
        if rotate_right:
            angle -= 7
        elif rotate_left:
            angle += 7
        if move:
            ship = ship_on_move
        else:
            ship = ship_on_stay

        for i in range(4):
            surface.blit(big_asteroid, (big_asrers[i][0], big_asrers[i][1]))
            # Движение астеройда в разные стороны
            if big_asrers[i][2] == 1:
                big_asrers[i][0] += 1
                big_asrers[i][1] += 1
            elif big_asrers[i][2] == 2:
                big_asrers[i][0] += 1
                big_asrers[i][1] -= 1
            elif big_asrers[i][2] == 3:
                big_asrers[i][0] -= 1
                big_asrers[i][1] += 1
            elif big_asrers[i][2] == 4:
                big_asrers[i][0] -= 1
                big_asrers[i][1] -= 1

            # Проверка на выход за пределы игрового поля и возвращение с другой стороны
            if big_asrers[i][0] < -40:
                big_asrers[i][0] = 840
                big_asrers[i][1] = 523 - big_asrers[i][1]
            elif big_asrers[i][1] < -40:
                big_asrers[i][0] = 800 - big_asrers[i][0]
                big_asrers[i][1] = 563
            elif big_asrers[i][0] > 840:
                big_asrers[i][0] = -40
                big_asrers[i][1] = 523 - big_asrers[i][1]
            elif big_asrers[i][1] > 563:
                big_asrers[i][0] = 800 - big_asrers[i][0]
                big_asrers[i][1] = -40
        surf = pygame.Surface((100, 100))
        surf.fill(WHITE)
        surf.set_colorkey((0, 0, 0))

        oldCenter = (400, 261.5)
        rotatedSurf = pygame.transform.rotate(ship, angle)
        rotRect = rotatedSurf.get_rect()
        rotRect.center = oldCenter
        surface.blit(rotatedSurf, rotRect)
        # hits = pygame.sprite.spritecollide(ship, big_asteroid, False)
        # for i in hits:
        #     print('Говно')

    # show score
    render_score = font_score.render(f'SCORE: {score}', True, pygame.Color('orange'))
    surface.blit(render_score, (5, 5))

    # show lives
    render_lives = font_lives.render(f'LIVES: {lives}', True, pygame.Color('orange'))
    surface.blit(render_lives, (680, 5))

    # animation
    pygame.display.flip()
    clock.tick(fps)
