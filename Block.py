import pygame
from Constants import *

# COLOR = pygame.Color("dark green")


class BLOCK:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BLOCK_W, BLOCK_H)
        self.block_img = pygame.image.load("graphics/GrassJoinHillRight&Left.png").convert_alpha()
        self.block_img = pygame.transform.scale(self.block_img, (BLOCK_W, BLOCK_H))

    def draw(self):
        screen.blit(self.block_img, (self.rect.topleft))

        # pygame.draw.rect(screen, self.COLOR, self.rect)
