import pygame
from Constants import *



class PLAYER:

    def __init__(self, player_number, x, y):
        self.w, self.h = PLAYER_W, PLAYER_H
        self.rect = pygame.Rect(x, y, self.w, self.h)
        self.direction = "right"
        self.x_vel = 5
        self.dx = 0
        self.dy = 0
        self.jump_count = 0
        self.jump_pressed = False
        self.dodge_ground = False
        self.player_number = player_number
        self.lives = PLAYER_LIVES
        self.previous_lives = self.lives
        self.touching_ground = False

        self.bullet_w, self.bullet_h = BULLET_W, BULLET_H
        self.bullet_damage = BULLET_DAMAGE
        self.bullets = []
        self.last_shot = pygame.time.get_ticks()
        self.bullet_cooldown = BULLET_COOLDOWN
        self.choose_default_skin()

    def choose_default_skin(self):
        if self.player_number == 1:
            self.original_img = pygame.image.load("graphics/player_red_pistol.png").convert_alpha()

        if self.player_number == 2:
            self.original_img = pygame.image.load("graphics/player_blue_pistol.png").convert_alpha()

    def choose_smg_skin(self):
        if self.player_number == 1:
            self.original_img = pygame.image.load("graphics/player_red_smg.png").convert_alpha()

        if self.player_number == 2:
            self.original_img = pygame.image.load("graphics/player_blue_smg.png").convert_alpha()

    def choose_sniper_skin(self):
        if self.player_number == 1:
            self.original_img = pygame.image.load("graphics/player_red_sniper.png").convert_alpha()

        if self.player_number == 2:
            self.original_img = pygame.image.load("graphics/player_blue_sniper.png").convert_alpha()
    def draw(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.player_img = pygame.transform.scale(self.original_img, (w, h))
        if self.direction == "left":
            flipped_image = pygame.transform.flip(self.player_img, True, False)
            screen.blit(flipped_image, self.rect)
        else:
            screen.blit(self.player_img, self.rect)


    def load_img(self):
        if self.player_number == 1:
            self.player_img = pygame.image.load("graphics/player_red.png").convert_alpha()

        if self.player_number == 2:
            self.player_img = pygame.image.load("graphics/player_blue.png").convert_alpha()

    def move_left(self):
        self.dx -= self.x_vel
        self.direction = "left"

    def move_right(self):
        self.dx += self.x_vel
        self.direction = "right"

    def handle_move(self):
        self.rect.x += self.dx
        self.dx = 0

    def gravity(self):
        self.dy += GRAVITY
        self.rect.y += self.dy

    def jump(self):
        self.dy = -JUMP_SPEED

    def shoot(self, BULLET):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_shot > self.bullet_cooldown:
            new_bullet = BULLET(self.rect.centerx, self.rect.centery,
                                self.bullet_w, self.bullet_h, self.direction,
                                self.player_number, self.bullet_damage)
            self.bullets.append(new_bullet)
            self.last_shot = current_time


    def collide_vertical(self, blocks):
        self.touching_ground = False
        for block in blocks:
            if (self.rect.colliderect(block.rect)
                    and self.dy >= 0
                    and self.rect.bottom < block.rect.top + self.dy + 3
                    and not self.dodge_ground):
                self.rect.bottom = block.rect.top
                self.touching_ground = True
                self.jump_count = 0
                self.dy = 0

    def stop_dodge(self, blocks):
        for block in blocks:
            if (self.dodge_ground
                    and self.rect.colliderect(block.rect)
                    and self.dy >= 0
                    and self.rect.top > block.rect.bottom - self.dy):
                self.dodge_ground = False

    def collide_border(self):
        if self.rect.centerx > screen.get_width():
            self.rect.centerx = 0
        if self.rect.centerx < 0:
            self.rect.centerx = screen.get_width()

    def collide_bottom(self):
        if self.rect.centery > screen.get_height():
            self.rect.centery = 0
        if self.rect.centery < 0:
            self.rect.centery = screen.get_height()

    def update(self, blocks):
        self.draw(self.rect.x, self.rect.y, self.w, self.h)
        self.gravity()
        self.collide_vertical(blocks)
        self.stop_dodge(blocks)
        self.collide_border()
        self.collide_bottom()
        self.handle_move()


