import math

import pygame
import random
from Constants import *
from Instances import *




class ITEM_BOX:
    def __init__(self):
        self.width = self.height = ITEM_W
        self.x_pos = self.y_pos = 0
        self.rand_pos()
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        # self.color = pygame.Color("yellow")
        self.item_running = False
        self.original_img = pygame.image.load("graphics/itemBox2.png")
        self.img = pygame.transform.scale(self.original_img, (self.width, self.height))


    def draw(self):
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        screen.blit(self.img, self.rect.topleft)

    def rand_pos(self):
        self.x_pos = random.randint(0, screen.get_width() - self.width)
        self.y_pos = random.randint(interface.rect_p1.h, screen.get_height() - self.height)


    def collide_player(self, player_1, player_2):
        self.item_running = False

        if self.rect.colliderect(player_1.rect):
            self.item_running = True
            self.collided_player = player_1
            self.choose_effect_or_weapon(self.collided_player)
            self.collided_player_time = pygame.time.get_ticks()


        if self.rect.colliderect(player_2.rect):
            self.item_running = True
            self.collided_player = player_2
            self.choose_effect_or_weapon(self.collided_player)
            self.collided_player_time = pygame.time.get_ticks()

    def choose_effect_or_weapon(self, collided_player):
        self.possible_items = [EFFECT, WEAPON]
        self.selected_item = random.choice(self.possible_items)
        self.item_instanz = self.selected_item(self.collided_player)
        self.item_instanz.choose_rand()
        self.item_running = True

    def check_duration(self, items):
        if pygame.time.get_ticks() > self.collided_player_time + ITEM_DUR:
            self.item_instanz.back_to_normal()
            print("effect over")
            items.remove(self)


    def update(self, player_1, player_2, items):
        if not self.item_running:
            self.draw()
            self.collide_player(player_1, player_2)

        else:
            self.check_duration(items)




class ITEM:
    def __init__(self, collided_player, possible_items):
        self.collided_player = collided_player
        self.possible_items = possible_items

    def choose_rand(self):
        self.selected_item = random.choice(self.possible_items)
        self.selected_item()

    def back_to_normal(self):
        self.collided_player.w = self.collided_player.h = PLAYER_W
        self.collided_player.bullet_w = self.collided_player.bullet_h = BULLET_W
        self.collided_player.bullet_cooldown = BULLET_COOLDOWN
        self.collided_player.bullet_damage = BULLET_DAMAGE
        self.collided_player.bullet_w, self.collided_player.bullet_h = BULLET_W, BULLET_H
        self.collided_player.choose_default_skin()




class EFFECT(ITEM):
    def __init__(self, collided_player):
        self.possible_effects = [self.player_get_bigger, self.player_get_smaller]
        super().__init__(collided_player, self.possible_effects)


    def player_change_size(self, size_factor_player, size_factor_bullet):
        self.collided_player.w *= size_factor_player
        self.collided_player.h *= size_factor_player
        self.collided_player.bullet_w *= size_factor_bullet
        self.collided_player.bullet_h *= size_factor_bullet

    def player_get_bigger(self):
        self.player_change_size(2, 2)
        self.collided_player.bullet_damage *= 2
    def player_get_smaller(self):
        self.player_change_size(0.5, 0.5)


class WEAPON(ITEM):
    def __init__(self, collided_player):
        self.possible_weapons = [self.smg, self.sniper]
        super().__init__(collided_player, self.possible_weapons)

    def smg(self):
        self.collided_player.bullet_cooldown = BULLET_COOLDOWN / 3
        self.collided_player.bullet_damage = BULLET_DAMAGE / 2
        self.collided_player.bullet_w = self.collided_player.bullet_h = BULLET_W / 4
        self.collided_player.choose_smg_skin()

    def sniper(self):
        self.collided_player.bullet_cooldown = BULLET_COOLDOWN * 3
        self.collided_player.bullet_damage = BULLET_DAMAGE * 3
        self.collided_player.bullet_w, self.collided_player.bullet_h = BULLET_W * 1.5, BULLET_H * 0.5
        self.collided_player.choose_sniper_skin()

