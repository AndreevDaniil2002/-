import pygame
from random import randrange
import math


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 6):
            img = pygame.image.load(f"img/exp{num}.png")
            img = pygame.transform.scale(img, (100, 100))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0

    def update(self):
        explosion_speed = 4
        # update explosion animation
        self.counter += 1

        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        # if the animation is complete, reset animation index
        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()


class Fon_asteroid(object):
    def __init__(self):
        self.fon_asteroid = pygame.image.load('img/fon_asteroids.png').convert()
        self.fon_asteroid.set_colorkey((255, 255, 255))
        self.aster_list = []

    def fon_aster_move(self):
        for i in range(len(self.aster_list)):
            surface.blit(self.fon_asteroid, (self.aster_list[i][0], self.aster_list[i][1]))
            self.aster_list[i][0] -= self.aster_list[i][2]
            if self.aster_list[i][0] < -50:
                self.aster_list[i][0] = 840

    def fon_aster_create(self):
        for i in range(25):
            aster_start_x = randrange(20, 1000)
            aster_start_y = randrange(0, 500)
            self.aster_list.append([aster_start_x, aster_start_y, randrange(1, 4)])


class Big_asteroid(object):
    def __init__(self):
        self.big_asteroid = pygame.image.load('img/big_asteroid.png').convert()
        self.big_asteroid.set_colorkey((255, 255, 255))
        self.aster_list = []
        self.aster_start_x = 0
        self.aster_start_y = 0
        self.angle = 0
        self.speed = 2
        self.count = 0

    def get_ast_rect(self, i):
        return self.aster_list[i][0].get_rect(center=(self.aster_list[i][1] + 40, self.aster_list[i][2] + 40))

    def creation(self, x, y):
        try:
            self.aster_start_x = randrange(80, int(x) - 100)
        except:
            self.aster_start_x = randrange(int(x) + 100)
        try:
            self.aster_start_y = randrange(80, int(y) - 100)
        except:
            self.aster_start_y = randrange(int(y) + 100)
        self.angle = randrange(0, 360)
        self.aster_list.append([self.big_asteroid, self.aster_start_x, self.aster_start_y, self.angle])

    def delete(self, i):
        self.count = 0
        self.aster_list.remove(
            [self.aster_list[i][0], self.aster_list[i][1], self.aster_list[i][2], self.aster_list[i][3]])

    def move(self, i):
        self.aster_list[i][1] = self.aster_list[i][1] + math.sin(self.aster_list[i][3]) * self.speed
        self.aster_list[i][2] = self.aster_list[i][2] + math.cos(self.aster_list[i][3]) * self.speed
        if self.aster_list[i][1] < -40:
            self.aster_list[i][1] = 840
            self.aster_list[i][2] = 523 - self.aster_list[i][2]
        elif self.aster_list[i][2] < -40:
            self.aster_list[i][1] = 800 - self.aster_list[i][1]
            self.aster_list[i][2] = 563
        elif self.aster_list[i][1] > 840:
            self.aster_list[i][1] = -40
            self.aster_list[i][2] = 523 - self.aster_list[i][2]
        elif self.aster_list[i][2] > 563:
            self.aster_list[i][1] = 800 - self.aster_list[i][1]
            self.aster_list[i][2] = -40


class Ship(object):
    def __init__(self):
        self.ship_on_stay = pygame.image.load('img/ship_on_stay.png').convert()
        self.ship_on_move = pygame.image.load('img/ship_on_move.png').convert()
        self.angle = 0
        self.speed = 3
        self.center = [400, 261.5]
        self.ship_on_stay.set_colorkey((255, 255, 255))
        self.ship_on_move.set_colorkey((255, 255, 255))

    def rotate(self, rotate):
        if rotate == 'right':
            self.angle -= 7
        elif rotate == 'left':
            self.angle += 7

    def get_ship(self, move):
        if move:
            return self.ship_on_move
        else:
            return self.ship_on_stay

    def get_ship_rect(self):
        return self.ship_on_stay.get_rect(center=self.center)

    def ship_move(self):
        self.center[0] = self.center[0] - math.sin(self.angle * math.pi / 180) * self.speed
        self.center[1] = self.center[1] - math.cos(self.angle * math.pi / 180) * self.speed
        if self.angle > 360:
            self.angle -= 360
        elif self.angle < -360:
            self.angle += 360

    def ship_rotate(self):
        surf = pygame.Surface((80, 80))
        surf.fill(WHITE)
        surf.set_colorkey((0, 0, 0))
        oldCenter = tuple(self.center)
        rotatedSurf = pygame.transform.rotate(ship, self.angle)
        rotRect = rotatedSurf.get_rect()
        rotRect.center = oldCenter
        surface.blit(rotatedSurf, rotRect)


class Laser(object):
    def __init__(self):
        self.laser = pygame.image.load('img/laser.png').convert()
        self.laser.set_colorkey((255, 255, 255))
        self.laser_angle = 0
        self.laser_speed = 6
        self.laser_list = []
        self.center = [0, 0]

    def creation(self):
        l_surf = pygame.Surface((20, 3))
        l_surf.fill(WHITE)
        l_surf.set_colorkey((0, 0, 0))
        l_oldCenter = tuple(self.center)
        l_rotatedSurf = pygame.transform.rotate(self.laser, self.laser_angle)
        l_rotRect = l_rotatedSurf.get_rect()
        l_rotRect.center = l_oldCenter
        self.laser_list.append([l_rotatedSurf, l_rotRect, self.laser_angle, self.center, self.laser, True, 50])

    def laser_move(self):
        if len(self.laser_list) != 0:
            for i in range(len(self.laser_list)):
                self.laser_list[i][3][0] -= math.sin(self.laser_list[i][2] * math.pi / 180) * self.laser_speed
                self.laser_list[i][3][1] -= math.cos(self.laser_list[i][2] * math.pi / 180) * self.laser_speed
                x, y = self.laser_list[i][3][0], self.laser_list[i][3][1]
                self.laser_list[i][1] = (x, y)


# Переменные для заставки
scale = True
size = 36
start = 220


def start_menu():
    global scale
    global size
    global start
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

img = pygame.image.load('img/1.png').convert()
font_score = font_lives = pygame.font.SysFont('Arial', 26, bold=True)

big_asteroid = Big_asteroid()
ship_object = Ship()
laser_object = Laser()
fon_aster = Fon_asteroid()
explosion_group = pygame.sprite.Group()
fon_aster.fon_aster_create()


def death():
    ship_object.center = [400, 261.5]
    big_asteroid.aster_list = []
    laser_object.laser_list = []
    ship_object.angle = 0
    for i in range(4):
        big_asteroid.creation(ship_object.center[0], ship_object.center[1])


def hlopok(x, y):
    explosion = Explosion(x, y)
    explosion_group.add(explosion)


# Создание больших астероидов

big_asters = big_asteroid.aster_list
asters = []

for i in range(4):
    big_asteroid.creation(ship_object.center[0], ship_object.center[1])

# Переменные для вращения корабля
start_flag = False
rotate_right = False
rotate_left = False
move = False

while True:
    surface.blit(img, (0, 0))
    explosion_group.draw(surface)
    explosion_group.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            start_flag = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                x = ship_object.center[0]
                y = ship_object.center[1]
                laser_object.center = [x, y]
                laser_object.laser_angle = ship_object.angle
                laser_object.creation()
            if event.key == pygame.K_RIGHT:
                rotate_right = True
            elif event.key == pygame.K_LEFT:
                rotate_left = True
            elif event.key == pygame.K_UP:
                move = True
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                rotate_right = rotate_left = False
            if event.key == pygame.K_UP:
                move = False

    fon_aster.fon_aster_move()
    if not start_flag:
        start_menu()
    else:
        if rotate_right:
            ship_object.rotate('right')
        elif rotate_left:
            ship_object.rotate('left')
        if move:
            ship = ship_object.ship_on_move
            ship_object.ship_move()
        else:
            ship = ship_object.ship_on_stay
        for i in range(len(big_asteroid.aster_list)):
            surface.blit(big_asteroid.aster_list[i][0], (big_asteroid.aster_list[i][1], big_asteroid.aster_list[i][2]))
            big_asteroid.move(i)
        ship_object.ship_rotate()

        for i in range(len(big_asteroid.aster_list)):
            aster_rect = big_asteroid.get_ast_rect(i)
            ship_rect = ship_object.get_ship_rect()
            if pygame.Rect.colliderect(ship_rect, aster_rect):
                hlopok(big_asteroid.aster_list[i][1] + 40, big_asteroid.aster_list[i][2] + 40)
                big_asteroid.delete(i)
                lives -= 1
                if lives == 0:
                    score = 0
                    lives = 3
                    start_flag = False
                    death()
                    break
                big_asteroid.creation(ship_object.center[0], ship_object.center[1])
        for i in range(len(laser_object.laser_list)):
            if laser_object.laser_list[i][5]:
                surface.blit(laser_object.laser_list[i][0], laser_object.laser_list[i][1])
                laser_rect = laser_object.laser_list[i][4].get_rect(center=tuple(laser_object.laser_list[i][3]))
                for j in range(len(big_asteroid.aster_list)):
                    aster_rect = big_asteroid.get_ast_rect(j)
                    if pygame.Rect.colliderect(laser_rect, aster_rect):
                        hlopok(big_asteroid.aster_list[j][1] + 40, big_asteroid.aster_list[j][2] + 40)
                        big_asteroid.delete(j)
                        laser_object.laser_list[i][5] = False
                        big_asteroid.creation(ship_object.center[0], ship_object.center[1])
                        score += 1
                laser_object.laser_list[i][6] -= 1
                if laser_object.laser_list[i][6] <= 0:
                    laser_object.laser_list[i][5] = False

        laser_object.laser_move()

    # show score
    render_score = font_score.render(f'SCORE: {score}', True, pygame.Color('orange'))
    surface.blit(render_score, (5, 5))

    # show lives
    render_lives = font_lives.render(f'LIVES: {lives}', True, pygame.Color('orange'))
    surface.blit(render_lives, (680, 5))

    # animation
    pygame.display.flip()
    clock.tick(fps)
