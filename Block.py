import pygame


class BLOCK:
    COLOR = pygame.Color("dark green")

    def __init__(self, x, y, width, height, BLOCK_W, BLOCK_H):
        self.rect = pygame.Rect(x, y, width, height)
        self.block_img = pygame.image.load("graphics/GrassJoinHillRight&Left.png").convert_alpha()
        self.block_img = pygame.transform.scale(self.block_img, (BLOCK_W, BLOCK_H))

    def draw(self, screen):
        screen.blit(self.block_img, (self.rect.topleft))
        # pygame.draw.rect(screen, self.COLOR, self.rect)
