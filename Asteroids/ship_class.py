import pygame


class Ship(object):
    def __init__(self):
        self.ship_on_stay = pygame.image.load('ship_on_stay.png').convert()
        self.ship_on_move = pygame.image.load('ship_on_move.png').convert()
        self.angle = 0
        self.center = (400, 261.5)
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
