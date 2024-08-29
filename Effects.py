import pygame
import random


class ITEM_BOX:
    def __init__(self, SCREEN_W, SCREEN_H, ITEM_W):
        self.width = self.height = ITEM_W
        self.color = pygame.Color("yellow")
        self.reroll_pos(SCREEN_W, SCREEN_H)
        self.collided = False
        self.effect_running = False
        self.effect_duration = 5 * 1000
        self.original_img = pygame.image.load("graphics/itemBox2.png")
        self.img = pygame.transform.scale(self.original_img, (self.width, self.height))

        self.effects = [
            self.player_get_bigger,
            self.player_get_smaller
        ]

    def draw(self, screen):
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)
        # pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.img, self.rect.topleft)

    def reroll_pos(self, SCREEN_W, SCREEN_H):
        self.x_pos = random.randint(0, SCREEN_W - self.width)
        self.y_pos = random.randint(self.height, SCREEN_H - self.height)

    def collide_player(self, player_1, player_2):
        self.collided_player = False

        if self.rect.colliderect(player_1.rect):
            self.collided = True
            self.collided_player = player_1
            self.rand_item()

        if self.rect.colliderect(player_2.rect):
            self.collided = True
            self.collided_player = player_2
            self.rand_item()

    def rand_item(self):
        # CHATGPT
        random_effect = random.choice(self.effects)
        random_effect()
        # CHATGPT
        self.effect_running = True
        self.collided_player_time = pygame.time.get_ticks()

    def check_duration(self, PLAYER_W, BULLET_W):
        if pygame.time.get_ticks() > self.collided_player_time + self.effect_duration:
            self.effect_running = False
            self.back_to_normal(PLAYER_W, BULLET_W)

    def player_change_size(self, size_factor_player, size_factor_bullet):
        self.collided_player.w *= size_factor_player
        self.collided_player.h *= size_factor_player
        self.collided_player.bullet_w *= size_factor_bullet
        self.collided_player.bullet_h *= size_factor_bullet

    def player_get_bigger(self):
        self.player_change_size(2, 2)

    def player_get_smaller(self):
        self.player_change_size(0.5, 0.5)

    def back_to_normal(self, PLAYER_W, BULLET_W):
        self.collided_player.w =  self.collided_player.h = PLAYER_W
        self.collided_player.bullet_w = self.collided_player.bullet_h =  BULLET_W


    def update(self, screen, player_1, player_2, PLAYER_W, PLAYER_H, BULLET_W, BULLET_H):
        if not self.collided:
            self.draw(screen)
            self.collide_player(player_1, player_2)
        elif self.effect_running:
            self.check_duration(PLAYER_W, BULLET_W)
