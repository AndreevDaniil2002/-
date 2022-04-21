import pygame
from random import randrange


class Big_asteroid(object):
    def __init__(self):
        self.big_asteroid = pygame.image.load('big_asteroid.png').convert()
        self.big_asteroid.set_colorkey((255, 255, 255))
        self.aster_list = []
        self.aster_start_x = 0
        self.aster_start_y = 0
        self.big_aster_angle = 0

    def creation(self):
        self.aster_start_x = randrange(80, 720)
        self.aster_start_y = randrange(80, 400)
        self.big_aster_angle = randrange(0, 360)
        self.aster_list.append([self.big_asteroid, self.aster_start_x, self.aster_start_y, self.big_aster_angle])