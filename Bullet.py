import pygame
from Constants import *
# from Main import interface



class BULLET:
    COLOR = pygame.Color("black")
    SPEED = 10

    # WIDTH, HEIGHT = 10, 5

    def __init__(self, x, y, w, h, direction, player_number, damage):
        self.rect = pygame.Rect(x, y, w, h)
        self.direction = direction
        self.bullet_number = player_number
        self.collided = False
        self.damage = damage


    def draw(self):
        pygame.draw.rect(screen, self.COLOR, self.rect)

    def collide_player(self, player_1, player_2, interface):
        if self.rect.colliderect(player_1.rect) and self.bullet_number == 2:
            self.collided = True
            player_1.lives -= self.damage
            interface.p1_lose_life(self.damage)

        if self.rect.colliderect(player_2.rect) and self.bullet_number == 1:
            self.collided = True
            player_2.lives -= self.damage
            interface.p2_lose_life(self.damage)

    def collide_bot(self, bot_1, player_1, interface):
        if self.rect.colliderect(bot_1.rect) and self.bullet_number == 1:
            self.collided = True
            bot_1.lives -= self.damage
            interface.p2_lose_life(self.damage)

        if self.rect.colliderect(player_1.rect) and self.bullet_number == 2:
            self.collided = True
            player_1.lives -= self.damage
            interface.p1_lose_life(self.damage)

    def update(self, player_1, player_2, interface):
        if not self.collided:
            if self.direction == "right":
                self.rect.x += self.SPEED
            elif self.direction == "left":
                self.rect.x -= self.SPEED
            self.draw()
            self.collide_player(player_1, player_2, interface)

    def update_bot(self, bot_1, player_1, interface):
        if not self.collided:
            if self.direction == "right":
                self.rect.x += self.SPEED
            elif self.direction == "left":
                self.rect.x -= self.SPEED
            self.draw()
            self.collide_bot(bot_1, player_1, interface)
