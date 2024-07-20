import pygame
import random

class ITEM:
    def __init__(self, SCREEN_W, SCREEN_H):
        self.width, self.height = 30, 30
        self.color = pygame.Color("yellow")
        self.reroll_pos(SCREEN_W, SCREEN_H)
        self.collided = False

    def draw(self, screen):
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height )
        pygame.draw.rect(screen, self.color, self.rect)

    def reroll_pos(self, SCREEN_W, SCREEN_H):
        self.x_pos = random.randint(0, SCREEN_W - self.width)
        self.y_pos = random.randint(self.height, SCREEN_H -self.height)

    def player_get_bigger(self, player_n, player_1, player_2):
        if player_n == 1:
            player_1.width, player_1.height = 100, 100
        if player_n == 2:
            player_2.width, player_2.height = 100, 100
            player_2.inside_block = False

    def collide_player(self,  player_1, player_2):
        if self.rect.colliderect(player_1.rect):
            self.collided = True
            print("collided player 1")
            self.player_get_bigger(1, player_1, player_2)

        if self.rect.colliderect(player_2.rect):
            self.collided = True
            print("collided player 2")
            self.player_get_bigger(2, player_1, player_2)

    def update(self, screen, player_1, player_2):
        if self.collided == False:
            self.draw(screen)
        self.collide_player(player_1, player_2)


