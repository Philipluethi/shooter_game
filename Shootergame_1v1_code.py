import pygame
import random
from block import BLOCK
from bullet import BULLET
from player import PLAYER

pygame.init()

SCREEN_W, SCREEN_H = 1000, 500
BLOCK_W, BLOCK_H = 50, 50
FPS = 60
GRAVITY = 1
JUMP_SPEED = 15
DODGE_SPEED = 15
JUMP_LIMIT = 2
BULLET_COOLDOWN = 1000 / 10
WINNER = None

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.update()
pygame.display.set_caption("Shooter Game 1v1")


class MAIN:
    def __init__(self):
        self.lives_font = pygame.font.SysFont("Arial", 30)
        self.title_font = pygame.font.SysFont("Arial", 50, True)
        self.subtitle_font = pygame.font.SysFont("Arial", 30)

    def check_keys(self):
        keys = pygame.key.get_pressed()
# P1
        if keys[pygame.K_LEFT]:
            player_1.move_left()

        if keys[pygame.K_RIGHT]:
            player_1.move_right()

        if keys[pygame.K_UP]:
            if player_1.jump_pressed == False and player_1.jump_count < JUMP_LIMIT:
                player_1.jump(JUMP_SPEED)
                player_1.jump_count += 1
                player_1.jump_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_1.jump_pressed = False

        if keys[pygame.K_SPACE]:
            player_1.shoot(BULLET, BULLET_COOLDOWN)

# P2

        if keys[pygame.K_a]:
            player_2.move_left()

        if keys[pygame.K_d]:
            player_2.move_right()

        if keys[pygame.K_w]:
            if player_2.jump_pressed == False and player_2.jump_count < JUMP_LIMIT:
                player_2.jump(JUMP_SPEED)
                player_2.jump_count += 1
                player_2.jump_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_2.jump_pressed = False

        if keys[pygame.K_CAPSLOCK]:
            player_2.shoot(BULLET, BULLET_COOLDOWN)

    def check_lives(self):
        global WINNER
        if player_1.lives < 1:
            WINNER = 2
            main.game_over()

        if player_2.lives < 1:
            WINNER = 1
            main.game_over()


    def random_map(self):
        for col in range(SCREEN_H // BLOCK_H):
            if col % random.randint(3, 4) == 0:
                for row in range(SCREEN_W // BLOCK_W):
                    if row % random.randint(5, 6) == 0:
                        blocks.append(BLOCK(row * BLOCK_H, col * BLOCK_H, random.randint(1, 5) * BLOCK_W, BLOCK_H))


    def draw_elements(self, blocks, player_1, player_2):
        player_1.draw(screen)
        player_2.draw(screen)
        for block in blocks:
            block.draw(screen)
        # F-String from Vid 3
        self.draw_text(f"P1: {player_1.lives}", self.lives_font, (255, 255, 255), SCREEN_W - 100, 50)
        self.draw_text(f"P2: {player_2.lives}", self.lives_font, (255, 255, 255), 100, 50)

    def draw_text(self, text, font, color, center_x, center_y):
        text_img = font.render(text, True, color)
        text_rect = text_img.get_rect(center=(center_x, center_y))
        screen.blit(text_img, text_rect)

    def game_over(self):
        winner_color = None
        screen.fill((0,0,0))
        if WINNER == 1:
            game_over_color = pygame.Color("red")
            winner_color = "RED"
        elif WINNER == 2:
            game_over_color = pygame.Color("blue")
            winner_color = "BLUE"

        self.draw_text("GAME OVER", self.title_font, game_over_color, SCREEN_W // 2, SCREEN_H // 2)
        self.draw_text(f"Player {winner_color} wins", self.subtitle_font, game_over_color, SCREEN_W // 2, SCREEN_H // 2 + 50)



# INSTANZEN
main = MAIN()
player_1 = PLAYER(1, 500, 0)
player_2 = PLAYER(2, 200, 0)
blocks = [
    BLOCK(0, SCREEN_H - BLOCK_H, SCREEN_W, BLOCK_H)
]
bullet = BULLET



# GAME LOOP
running = True
main.random_map()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.Color("light blue"))

    main.draw_elements(blocks, player_1, player_2)
    main.check_keys()
    main.check_lives()
    player_1.update(GRAVITY, blocks, screen, player_1, player_2)
    player_2.update(GRAVITY, blocks, screen, player_1, player_2)

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()