import pygame
from Constants import *
from Player import PLAYER



class INTERFACE:
    def __init__(self):
        self.w = screen.get_width() / 4
        self.h = 50
        self.border = 5
        self.rect_p2 = pygame.Rect(10, 10, self.w, self.h)
        self.rect_p1 = pygame.Rect(screen.get_width() - 10 - self.w, 10, self.w, self.h)

        self.rect_p2_lives = pygame.Rect(15, 15, self.w - self.border*2 , self.h - self.border*2)
        self.rect_p1_lives = pygame.Rect(screen.get_width() - self.w - 5, 15, self.w - self.border*2, self.h - self.border*2)
        self.info_rect = pygame.Rect(0, 0, screen.get_width(), screen.get_height())

        self.info_img = pygame.image.load("graphics/info.png")
        self.info_img_ratio = self.info_img.get_height() / self.info_img.get_width()
        self.info_img = pygame.transform.scale(self.info_img, (screen.get_width(), screen.get_width() * self.info_img_ratio))


    def draw_p1(self):
        pygame.draw.rect(screen, (255, 255, 255), self.rect_p1)
        pygame.draw.rect(screen, pygame.Color("red"), self.rect_p1_lives)

    def draw_p2(self):
        pygame.draw.rect(screen, (255, 255, 255), self.rect_p2)
        pygame.draw.rect(screen, pygame.Color("blue"), self.rect_p2_lives)

    def p1_lose_life(self, damage):
        self.rect_p1_lives.w -= (damage / PLAYER_LIVES) * (self.w - self.border*3)

    def p2_lose_life(self, damage):
        self.rect_p2_lives.w -= (damage / PLAYER_LIVES) * (self.w - self.border*3)

    def draw_info(self):
        screen.blit(self.info_img, self.info_rect)

    def update(self):
        self.draw_p1()
        self.draw_p2()
