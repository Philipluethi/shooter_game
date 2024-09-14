import random

import pygame.time

from Player import *

class BOT(PLAYER):
    pass
    def __init__(self):
        # self.original_img = pygame.image.load("graphics/blue2.png").convert_alpha()
        self.last_movement_time = pygame.time.get_ticks()
        self.last_delay = pygame.time.get_ticks()
        super().__init__(2, PLAYER_2_START_X, PLAYER_2_START_Y)

    def random_movements(self, BULLET):

        self.possible_methods = [self.move_left, self.move_right]
        self.random_method = random.choice(self.possible_methods)
        self.random_method()


        # if pygame.time.get_ticks() > self.last_movement_time + self.movement_intervall:
        #
        # else:
        #     self.last_movement_time = pygame.time.get_ticks()


    def update_controlls(self, BULLET):
        self.random_movements(BULLET)
