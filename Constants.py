import pygame
import math
import random
from random import choice


FPS = 60
SCREEN_W = 1000
SCREEN_H = SCREEN_W // 2
SCREEN_RATIO = SCREEN_H / SCREEN_W

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
screen_rect = screen.get_rect()
pygame.display.set_caption("Bullet Rush")
clock = pygame.time.Clock()


BLOCK_W = BLOCK_H = screen.get_height() // 7

PLAYER_W = PLAYER_H = BLOCK_H * 0.9
PLAYER_2_START_X = screen.get_width() / 4
PLAYER_2_START_Y = screen.get_height() / 2
PLAYER_1_START_X = screen.get_width() - PLAYER_2_START_X
PLAYER_1_START_Y = PLAYER_2_START_Y

PLAYER_LIVES = 100
BULLET_DAMAGE = 4
GRAVITY = 1
BULLET_W = PLAYER_W * 0.5
BULLET_H = BULLET_W / 2
JUMP_SPEED = PLAYER_W / 4
JUMP_LIMIT = 2
BULLET_COOLDOWN = 1000 / 3


ITEM_COUNT = 2
ITEM_W = int(BLOCK_W * 0.5)
ITEM_DUR = 1000 * 5



