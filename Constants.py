import pygame

FPS = 60
SCREEN_W, SCREEN_H = 1200, 600

BLOCK_W = BLOCK_H = SCREEN_H // 7

PLAYER_W = PLAYER_H = BLOCK_H * 0.9
PLAYER_LIVES = 5
GRAVITY = 1
BULLET_W = PLAYER_W * 0.5
BULLET_H = BULLET_W / 2
JUMP_SPEED = PLAYER_W / 4.5
JUMP_LIMIT = 2
BULLET_COOLDOWN = 1000 / 3

ITEM_W = int(BLOCK_W * 0.5)



screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Bullet Rush")
clock = pygame.time.Clock()