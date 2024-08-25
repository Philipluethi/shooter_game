import pygame
import random


class ITEM_BOX:
    def __init__(self, SCREEN_W, SCREEN_H):
        self.width, self.height = 30, 30
        self.color = pygame.Color("yellow")
        self.reroll_pos(SCREEN_W, SCREEN_H)
        self.collided = False
        self.effect_running = False
        self.effect_duration = 5 * 1000
        self.img = pygame.image.load("graphics/itemBox.png")
        self.img = pygame.transform.scale(self.img, (self.width, self.height))

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
            print("collided player 1")
            self.rand_item()

        if self.rect.colliderect(player_2.rect):
            self.collided = True
            self.collided_player = player_2
            print("collided player 2")
            self.rand_item()

    def rand_item(self):
        # CHATGPT
        random_effect = random.choice(self.effects)
        random_effect()
        # CHATGPT
        self.effect_running = True
        print("effect running")
        self.collided_player_time = pygame.time.get_ticks()

    def check_duration(self, PLAYER_W, PLAYER_H, BULLET_W, BULLET_H):
        if pygame.time.get_ticks() > self.collided_player_time + self.effect_duration:
            self.effect_running = False
            print("effect stop")
            self.back_to_normal(PLAYER_W, PLAYER_H, BULLET_W, BULLET_H)

    def player_change_size(self, w, h, bullet_w, bullet_h):
        self.collided_player.w, self.collided_player.h = w, h
        self.collided_player.bullet_w, self.collided_player.bullet_h = bullet_w, bullet_h

    def player_get_bigger(self):
        self.player_change_size(80, 80, 30, 15)

    def player_get_smaller(self):
        self.player_change_size(20, 20, 10, 5)

    def back_to_normal(self, PLAYER_W, PLAYER_H, BULLET_W, BULLET_H):
        self.player_change_size(PLAYER_W, PLAYER_H, BULLET_W, BULLET_H)

    def update(self, screen, player_1, player_2, PLAYER_W, PLAYER_H, BULLET_W, BULLET_H):
        if not self.collided:
            self.draw(screen)
            self.collide_player(player_1, player_2)
        if self.effect_running:
            self.check_duration(PLAYER_W, PLAYER_H, BULLET_W, BULLET_H)
