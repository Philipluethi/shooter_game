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

    def update(self, screen, player_1, player_2):
        if self.collided == False:
            self.draw(screen)
        if self.rect.colliderect(player_1.rect):
            self.collided = True
            print("collided player 1")

