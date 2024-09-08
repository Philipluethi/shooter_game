import pygame
import random
from Constants import *




class ITEM_BOX:
    def __init__(self):
        self.width = self.height = ITEM_W
        self.x_pos = self.y_pos = 0
        self.rand_pos()
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        self.color = pygame.Color("yellow")
        self.item_running = False
        self.original_img = pygame.image.load("graphics/itemBox2.png")
        self.img = pygame.transform.scale(self.original_img, (self.width, self.height))


    def draw(self):
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        # pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.img, self.rect.topleft)

    def rand_pos(self):
        self.x_pos = random.randint(0, SCREEN_W - self.width)
        self.y_pos = random.randint(self.height, SCREEN_H - self.height)


    def collide_player(self, player_1, player_2):
        self.item_running = False

        if self.rect.colliderect(player_1.rect):
            self.item_running = True
            self.collided_player = player_1
            self.choose_effect_or_weapon(self.collided_player)


        if self.rect.colliderect(player_2.rect):
            self.item_running = True
            self.collided_player = player_2
            self.choose_effect_or_weapon(self.collided_player)

    def choose_effect_or_weapon(self, collided_player):
        self.possible_items = [EFFECT, WEAPON]

        # CHATGPT
        self.selected_item = random.choice(self.possible_items)

        # print(self.selected_item)
        # selected_item(collided_player)
        self.item_instanz = self.selected_item(self.collided_player)
        self.item_instanz.choose_rand()
        self.item_running = True
        self.collided_player_time = pygame.time.get_ticks()


    # def check_duration(self):
    #     if pygame.time.get_ticks() > self.collided_player_time + ITEM_DUR:
    #         self.effect_running = False
    #         self.back_to_normal()



    def update(self, player_1, player_2):
        if not self.item_running:
            self.draw()
            self.collide_player(player_1, player_2)
            # self.check_duration()



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
        print("bigger")

    def player_get_smaller(self):
        self.player_change_size(0.5, 0.5)
        print("smaller")


class WEAPON(ITEM):
    def __init__(self, collided_player):
        self.possible_weapons = [self.smg, self.sniper]
        super().__init__(collided_player, self.possible_weapons)

    def smg(self):
        self.collided_player.bullet_cooldown = 1000 / 10
        self.collided_player.bullet_damage = BULLET_DAMAGE / 2
        self.collided_player.bullet_w = self.collided_player.bullet_h = BULLET_W / 4

        print("smg")

    def sniper(self):
        print("sniper")
