import random

import pygame.time

from Player import *

class BOT(PLAYER):
    pass
    def __init__(self):
        super().__init__(2, PLAYER_2_START_X, PLAYER_2_START_Y)

        self.possible_methods = [self.move_left, self.move_right]

        self.movement_delay = 20
        self.last_movement_delay = pygame.time.get_ticks()

        self.jump_intervall = 1000
        self.last_jump_time = pygame.time.get_ticks()

        self.movement_intervall = 200
        self.last_movement_time = pygame.time.get_ticks()

        self.shoot_intervall = BULLET_COOLDOWN * 2
        self.last_shoot_time = pygame.time.get_ticks()

    def repeat_method(self, method, intervall, times, delay):
        last_movement_time = pygame.time.get_ticks()
        last_movement_delay = pygame.time.get_ticks()

        if pygame.time.get_ticks() > last_movement_time + intervall:
            for i in range(times):
                if pygame.time.get_ticks() > last_movement_delay + delay:
                    method()
                    delay = pygame.time.get_ticks()
            last_movement_time = pygame.time.get_ticks()


    def random_movements(self, BULLET, player_1):
        self.random_method = random.choice(self.possible_methods)

        if pygame.time.get_ticks() > self.last_movement_time + self.movement_intervall:
            for i in range(random.randint(0,5)):
                if pygame.time.get_ticks() > self.last_movement_delay + self.movement_delay:
                    self.random_method()
                    self.movement_delay = pygame.time.get_ticks()
            self.last_movement_time = pygame.time.get_ticks()

        if pygame.time.get_ticks() > self.last_jump_time + self.jump_intervall:
            for i in range(random.randint(0,1)):
                self.jump()
                self.last_jump_time = pygame.time.get_ticks()

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
