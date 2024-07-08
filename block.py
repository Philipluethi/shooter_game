import pygame

class BLOCK:
    COLOR = pygame.Color("dark green")
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.COLOR, self.rect)