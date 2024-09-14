import random

import pygame.time

from Player import *

class BOT(PLAYER):
    pass
    def __init__(self):
        super().__init__(2, PLAYER_2_START_X, PLAYER_2_START_Y)

        self.possible_methods = [self.move_left, self.move_right]
        self.last_movement_time = pygame.time.get_ticks()
        # self.movement_delay = 500
        # self.last_movement_delay = pygame.time.get_ticks()
        self.last_jump_time = pygame.time.get_ticks()

        self.last_shoot_time = pygame.time.get_ticks()

    def random_movements(self, BULLET, player_1):
        # self.random_method = random.choice(self.possible_methods)
        self.movement_intervall = 2500

        if pygame.time.get_ticks() > self.last_movement_time + self.movement_intervall:
            self.dodge_ground = True
            self.last_movement_time = pygame.time.get_ticks()

        self.jump_intervall = 2000

        if pygame.time.get_ticks() > self.last_jump_time + self.jump_intervall:
            self.jump()
            self.last_jump_time = pygame.time.get_ticks()

        self.shoot_intervall = BULLET_COOLDOWN * 2

        if pygame.time.get_ticks() > self.last_shoot_time + self.shoot_intervall:
            for i in range(1):
                self.shoot(BULLET)
                self.look_to_p1(player_1)
            self.last_shoot_time = pygame.time.get_ticks()


    def look_to_p1(self, player_1):
        if self.rect.centerx > player_1.rect.centerx:
            self.direction = "left"
        else:
            self.direction = "right"


    def update_controlls(self, BULLET, player_1):
        self.random_movements(BULLET, player_1)
