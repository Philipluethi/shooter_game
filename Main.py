import pygame
import random
from Constants import *
from Block import BLOCK
from Bullet import BULLET
from Player import PLAYER
from Effects import *
from Interface import INTERFACE
from Bot import BOT
from Instances import *
from pygame.locals import *

pygame.init()

class MAIN:
    def __init__(self):
        self.lives_font = pygame.font.SysFont("Arial", 30, True)
        self.title_font = pygame.font.SysFont("Arial", 50, True)
        self.subtitle_font = pygame.font.SysFont("Arial", 30)
        self.winner = None
        self.game_over = False

        self.background_img = pygame.image.load("graphics/background1.png").convert_alpha()
        self.background_img = pygame.transform.scale(self.background_img, (screen.get_width(), screen.get_height()))
        self.t_pressed = False


    def test(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_t] and not self.t_pressed:
            # weapon = WEAPON(player_1)
            # weapon.sniper()
            # weapon = WEAPON(player_2)
            # weapon.smg()
            effect = EFFECT(player_1)
            effect.player_change_size(2,2)
            self.t_pressed = True


    def update_elements(self):
        screen.blit(self.background_img, (0, 0))

        for block in blocks:
            block.draw()
        interface.update()

        for bullet in player_1.bullets:
            bullet.update(player_1, player_2, interface)

        for bullet in player_2.bullets:
            bullet.update(player_1, player_2, interface)

        player_1.update(blocks)
        player_2.update(blocks)
        # bot_1.update(blocks)
        # bot_1.update_controlls(BULLET)


        for item in items:
            item.update(player_1, player_2, items)

        # F-String from Vid 3
        self.draw_text(player_1.lives, self.lives_font, (0, 0, 0), screen.get_width() - 100, interface.rect_p1_lives.centery)
        self.draw_text(player_2.lives, self.lives_font, (0, 0, 0), 100, interface.rect_p2_lives.centery)




    def update_elements_1p(self):
        for block in blocks:
            block.draw()

        interface.update()

        for bullet in player_1.bullets:
            bullet.update_bot(bot_1, player_1, interface)

        for bullet in bot_1.bullets:
            bullet.update_bot(bot_1, player_1, interface)

        player_1.update(blocks)
        bot_1.update(blocks)
        bot_1.update_controlls(BULLET, player_1)

        for item in items:
            item.update(player_1, player_2, items)

        # F-String from Vid 3
        self.draw_text(player_1.lives, self.lives_font, (0, 0, 0), screen.get_width() - 100, interface.rect_p1_lives.centery)
        self.draw_text(bot_1.lives, self.lives_font, (0, 0, 0), 100, interface.rect_p2_lives.centery)

    def check_keys(self):
        # P1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_1.move_left()

        if keys[pygame.K_RIGHT]:
            player_1.move_right()

        if keys[pygame.K_UP]:
            if not player_1.jump_pressed and player_1.jump_count < JUMP_LIMIT:
                player_1.jump()
                player_1.jump_count += 1
                player_1.jump_pressed = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_1.jump_pressed = False

        if keys[pygame.K_SPACE]:
            player_1.shoot(BULLET)



        if player_1.touching_ground:
            if keys[pygame.K_DOWN]:
                player_1.dodge_ground = True

        # P2

        if keys[pygame.K_a]:
            player_2.move_left()

        if keys[pygame.K_d]:
            player_2.move_right()

        if keys[pygame.K_w]:
            if not player_2.jump_pressed and player_2.jump_count < JUMP_LIMIT:
                player_2.jump()
                player_2.jump_count += 1
                player_2.jump_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_2.jump_pressed = False

        if keys[pygame.K_CAPSLOCK]:
            player_2.shoot(BULLET)

        if player_2.touching_ground:
            if keys[pygame.K_s]:
                player_2.dodge_ground = True

        # MAP
        if keys[pygame.K_r]:
            blocks[1:] = []
            main.random_map()

        # ITEM
        for item in items:
            for block in blocks:
                if keys[pygame.K_i]:
                    item.rand_pos()

        # INFO
        if keys[pygame.K_h]:
            interface.draw_info()



    def check_lives(self):

        if player_1.lives < 1:
            self.winner = 2
            self.game_over = True

        if player_2.lives < 1 or bot_1.lives < 1:
            self.winner = 1
            self.game_over = True
        #
        # if player_1.lives < player_1.previous_lives:
        #     interface.p1_lose_life()
        #     player_1.previous_lives = player_1.lives
        #
        # if player_2.lives < player_2.previous_lives:
        #     interface.p2_lose_life()
        #     player_2.previous_lives = player_2.lives

    def random_map(self):
        last_row = (screen.get_height() // BLOCK_H) * BLOCK_H - BLOCK_H
        for col in range(screen.get_width() // BLOCK_W + 1):
            blocks.append(BLOCK(BLOCK_W * col, last_row))

        for col in range(screen.get_height() // BLOCK_H):
            if col % 2 == 0:
                for row in range(screen.get_width() // BLOCK_W):
                    if row % random.randint(1, 3) == 0:
                        blocks.append(BLOCK(row * BLOCK_H, col * BLOCK_H))



        for item in items:
            # long_rect = pygame.Rect(item.rect.x, 0, item.rect.w, item.rect.h + screen.get_height())
            # pygame.draw.rect(screen, (0, 0, 0), long_rect)

            for block in blocks:
                if item.rect.colliderect(block.rect):
                    item.rand_pos()

            if player_1.rect.colliderect(item.rect.x, 0, item.rect.w, item.rect.h + screen.get_height()):
                item.rand_pos()

            if player_2.rect.colliderect(item.rect.x, 0, item.rect.w, item.rect.h + screen.get_height()):
                item.rand_pos()

    def random_items(self):
        if len(items) < ITEM_COUNT:
            items.append(ITEM_BOX())


    # FROM VID 3
    def draw_text(self, text, font, color, center_x, center_y):
        text_img = font.render(str(text), True, color)
        text_rect = text_img.get_rect(center=(center_x, center_y))
        screen.blit(text_img, text_rect)

    def update(self):
        self.update_elements()
        self.check_keys()
        self.check_lives()
        self.random_items()
        self.test()

    def update_1p(self):
        self.update_elements_1p()
        self.check_keys()
        self.check_lives()
        self.random_items()
        self.test()


main = MAIN()

# GAME LOOPS

start_screen = True
two_player = False
one_player = False
main.random_map()

while start_screen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start_screen = False
    screen.fill(pygame.Color("white"))
    main.draw_text("CHOOSE A GAME MODE", main.title_font, pygame.Color("black"), screen.get_width() // 2, screen.get_height()//2-150)
    main.draw_text("press 1 for single player",main.subtitle_font, pygame.Color("black"),screen.get_width()//2,screen.get_height()//2)
    main.draw_text("press 2 for two-player",main.subtitle_font,pygame.Color("black"), screen.get_width()//2,screen.get_height()//2+50)
    main.draw_text("hold h for info", main.subtitle_font, pygame.Color("black"), screen.get_width() // 2,screen.get_height()//2+100)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_2]:
        start_screen = False
        two_player = True
    if keys[pygame.K_1]:
        start_screen = False
        one_player = True
    if keys[pygame.K_h]:
        interface.draw_info()
    clock.tick(FPS)
    pygame.display.update()


# MAIN-LOOP

while two_player:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            two_player = False
    if main.game_over:
        two_player = False

    # screen.fill(pygame.Color("light blue"))
    main.update()


    pygame.display.update()
    clock.tick(FPS)

while one_player:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            one_player = False
    if main.game_over:
        one_player = False

    screen.fill(pygame.Color("light blue"))
    screen.blit(main.background_img, (0, 0))
    main.update_1p()

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
        winner_color = "red"
        player_1.update(blocks)

    if main.winner == 2:
        winner_color = "blue"
        player_2.update(blocks)

    main.draw_text(f"Player {main.winner} wins", main.title_font, pygame.Color(winner_color), screen.get_width() // 2, screen.get_height() // 2 - 50)
    main.draw_text("GAME OVER", main.subtitle_font, pygame.Color(winner_color), screen.get_width() // 2, screen.get_height() // 2)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
