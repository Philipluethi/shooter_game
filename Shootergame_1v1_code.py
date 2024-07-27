import pygame
import random
from block import BLOCK
from bullet import BULLET
from player import PLAYER
from item_box import ITEM_BOX

pygame.init()

FPS = 60
SCREEN_W, SCREEN_H = 1000, 500
BLOCK_W, BLOCK_H = 50, 50
PLAYER_W, PLAYER_H = 40, 40
BULLET_W, BULLET_H = 10, 5

GRAVITY = 1
JUMP_SPEED = 15
JUMP_LIMIT = 2
BULLET_COOLDOWN = 1000 / 10


clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.update()
pygame.display.set_caption("Shooter Game 1v1")



class MAIN:
    def __init__(self):
        self.lives_font = pygame.font.SysFont("Arial", 30, True)
        self.title_font = pygame.font.SysFont("Arial", 50, True)
        self.subtitle_font = pygame.font.SysFont("Arial", 30)
        self.winner = None
        self.game_over = False

        # self.game_over_flag = False

    def print(self):
        pass
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

        if player_1.touching_ground == True:
            if keys[pygame.K_DOWN]:
                player_1.dodge_ground = True


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

        if player_2.touching_ground == True:
            if keys[pygame.K_s]:
                player_2.dodge_ground = True


    def check_lives(self):

        if player_1.lives < 1:
            self.winner = 2
            self.game_over = True

        if player_2.lives < 1:
            self.winner = 1
            self.game_over = True



    def random_map(self):
        for col in range(SCREEN_H // BLOCK_H):
            if col % random.randint(1,2) == 0:
                for row in range(SCREEN_W // BLOCK_W):
                    if row % random.randint(1, 5) == 0:
                        blocks.append(BLOCK(row * BLOCK_H, col * BLOCK_H, BLOCK_W, BLOCK_H))


    def draw_text(self, text, font, color, center_x, center_y):
        text_img = font.render(text, True, color)
        text_rect = text_img.get_rect(center=(center_x, center_y))
        screen.blit(text_img, text_rect)

    def draw_elements(self, blocks, player_1, player_2):
        for block in blocks:
            block.draw(screen)
        player_1.draw(screen, player_1.rect.x, player_1.rect.y, player_1.width, player_1.height)
        player_2.draw(screen, player_2.rect.x, player_2.rect.y, player_2.width, player_2.height)
# F-String from Vid 3
        self.draw_text(f"P1: {player_1.lives}", self.lives_font, (0,0,0), SCREEN_W - 100, 50)
        self.draw_text(f"P2: {player_2.lives}", self.lives_font, (0,0,0), 100, 50)
        self.print()


# INSTANZEN
main = MAIN()
player_1 = PLAYER(1, 500, 0,  PLAYER_W, PLAYER_H, BULLET_W, BULLET_H)
player_2 = PLAYER(2, 200, 0,  PLAYER_W, PLAYER_H, BULLET_W, BULLET_H)
blocks = [
    BLOCK(0, SCREEN_H - BLOCK_H, SCREEN_W, BLOCK_H)
]
bullet = BULLET
item = ITEM_BOX(SCREEN_W, SCREEN_H)


# GAME LOOPS

start_screen = True
two_player = False
one_player = False
main.random_map()

while start_screen:
    screen.fill(pygame.Color("white"))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start_screen = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_2]:
        print("2-PLAYER")
        start_screen = False
        two_player = True

    if keys[pygame.K_1]:
        print("SINGLE PLAYER")
        start_screen = False
        one_player = True

    main.draw_text("CHOOSE A GAME MODE", main.title_font, pygame.Color("black"), SCREEN_W // 2, SCREEN_H // 2 - 150)
    main.draw_text("press 1 for single player", main.subtitle_font, pygame.Color("black"), SCREEN_W // 2, SCREEN_H // 2)
    main.draw_text("press 2 for two-player", main.subtitle_font, pygame.Color("black"), SCREEN_W // 2, SCREEN_H // 2 + 50)

    clock.tick(FPS)
    pygame.display.update()

while two_player:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            two_player = False
    screen.fill(pygame.Color("light blue"))
    if main.game_over == True:
        two_player = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        blocks[1:] = []
        main.random_map()

    main.draw_elements(blocks, player_1, player_2)
    main.check_keys()
    item.update(screen, player_1, player_2)
    player_1.update(GRAVITY, blocks, screen, player_1, player_2, SCREEN_W, SCREEN_H)
    player_2.update(GRAVITY, blocks, screen, player_1, player_2, SCREEN_W, SCREEN_H)
    main.check_lives()

    for block in blocks:
        if keys[pygame.K_i] or item.rect.colliderect(block.rect):
            item.reroll_pos(SCREEN_W, SCREEN_H)

    pygame.display.update()
    clock.tick(FPS)

while one_player:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            one_player = False
    screen.fill(pygame.Color("grey"))

    player_1.draw(screen, player_1.rect.x, player_1.rect.y, player_1.width, player_1.height)
    for block in blocks:
        block.draw(screen)
    main.check_keys()
    main.check_lives()
    player_1.update(GRAVITY, blocks, screen, player_1, player_2, SCREEN_W, SCREEN_H)

    pygame.display.update()
    clock.tick(FPS)

while main.game_over:
    screen.fill(pygame.Color("black"))
    winner_color = None
    main.check_keys()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main.game_over = False

    if main.winner == 1:
        game_over_color = pygame.Color("red")
        winner_color = "RED"
        player_1.draw(screen, player_1.rect.x, player_1.rect.y, player_1.width, player_1.height)
        player_1.update(GRAVITY, blocks, screen, player_1, player_2, SCREEN_W, SCREEN_H)


    if main.winner == 2:
        game_over_color = pygame.Color("blue")
        winner_color = "BLUE"
        player_2.draw(screen, player_2.rect.x, player_2.rect.y, player_2.width, player_2.height)
        player_2.update(GRAVITY, blocks, screen, player_1, player_2, SCREEN_W, SCREEN_H)

    main.draw_text(f"Player {winner_color} wins", main.title_font, game_over_color, SCREEN_W // 2, SCREEN_H // 2 - 50)
    main.draw_text("GAME OVER", main.subtitle_font, game_over_color, SCREEN_W // 2, SCREEN_H // 2)

    pygame.display.update()
    clock.tick(FPS)


pygame.quit()