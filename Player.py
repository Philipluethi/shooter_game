import pygame
from Constants import *
# from Instances import blocks



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



        if self.player_number == 1:
            # self.color = pygame.Color("red")
            self.original_img = pygame.image.load("graphics/red2.png").convert_alpha()

        if self.player_number == 2:
            # self.color = pygame.Color("blue")
            self.original_img = pygame.image.load("graphics/blue2.png").convert_alpha()

    def draw(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.player_img = pygame.transform.scale(self.original_img, (w, h))
        if self.direction == "left":
            flipped_image = pygame.transform.flip(self.player_img, True, False)
            screen.blit(flipped_image, self.rect)
        else:
            screen.blit(self.player_img, self.rect)

        # pygame.draw.rect(screen, self.color, self.rect)


    def load_img(self):
        if self.player_number == 1:
            self.player_img = pygame.image.load("graphics/red2.png").convert_alpha()

        if self.player_number == 2:
            self.player_img = pygame.image.load("graphics/blue2.png").convert_alpha()

    def move_left(self):
        # if not self.collided_left:
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
            bullet_x = self.rect.centerx
            bullet_y = self.rect.centery

            new_bullet = BULLET(bullet_x, bullet_y, self.bullet_w, self.bullet_h, self.direction, self.player_number, self.bullet_damage)
            self.bullets.append(new_bullet)
            self.last_shot = current_time

    def check_inside_block(self, blocks):
        pass
        self.inside_block = False

        for block in blocks:
            if (self.rect.colliderect(block.rect)
                    and self.rect.top > block.rect.top
                    and self.rect.left < block.rect.centerx
                    and self.rect.right > block.rect.centerx
                    and self.h < block.rect.h):
                self.inside_block = True


    def collide_vertical(self, blocks):
        self.touching_ground = False

        for block in blocks:
            if (self.rect.colliderect(block.rect)
                    and self.dy >= 0
                    and self.rect.bottom < block.rect.top + self.dy + 5
                    and not self.dodge_ground
                    # and not self.inside_block
            ):
                self.rect.bottom = block.rect.top
                self.touching_ground = True
                self.jump_count = 0
                self.dy = 0

    def stop_dodge(self, blocks):
        for block in blocks:
            if (self.dodge_ground
                    and self.rect.colliderect(block.rect)
                    and self.rect.bottom < block.rect.bottom
                    and self.rect.bottom > block.rect.centery):
                self.dodge_ground = False

    def collide_border(self):
        if self.rect.centerx > SCREEN_W:
            self.rect.centerx = 0
        if self.rect.centerx < 0:
            self.rect.centerx = SCREEN_W

    def collide_bottom(self):
        if self.rect.centery > SCREEN_H:
            self.rect.centery = 0
        if self.rect.centery < 0:
            self.rect.centery = SCREEN_H

    def update(self, blocks):
        self.draw(self.rect.x, self.rect.y, self.w, self.h)
        self.gravity()
        self.check_inside_block(blocks)
        self.collide_vertical(blocks)
        self.stop_dodge(blocks)
        self.collide_border()
        self.collide_bottom()
        self.handle_move()


        # self.collide_horizontal(blocks)
