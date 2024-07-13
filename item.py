import pygame
import random

class ITEM:
    def __init__(self, SCREEN_W, SCREEN_H):
        self.width, self.height = 30, 30
        self.color = pygame.Color("yellow")
        self.reroll_pos(SCREEN_W, SCREEN_H)

    def draw(self, SCREEN):
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height )
        pygame.draw.rect(SCREEN, self.color, self.rect)

    def reroll_pos(self, SCREEN_W, SCREEN_H):
        self.x_pos = random.randint(0, SCREEN_W - self.width)
        self.y_pos = random.randint(self.height, SCREEN_H -self.height)
