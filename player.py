import pygame

class PLAYER:

    def __init__(self, player_number, x, y, PLAYER_W, PLAYER_H, BULLET_W, BULLET_H):
        self.width, self.height = PLAYER_W, PLAYER_H
        self.bullet_w, self.bullet_h = BULLET_W, BULLET_H

        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.direction = "right"
        self.x_vel = 5
        self.dx = 0
        self.y_vel = 0
        self.jump_count = 0
        self.jump_pressed = False
        self.dodge_ground = False
        self.bullets = []
        self.last_shot = pygame.time.get_ticks()
        self.player_number = player_number
        self.lives = 10
        self.touching_ground = False


        if self.player_number == 1:
            self.color = pygame.Color("red")
        if self.player_number == 2:
            self.color = pygame.Color("blue")

    def draw(self, screen, x, y, width, height):
        self.rect = pygame.Rect(x, y, self.width, self.height)
        pygame.draw.rect(screen, self.color, self.rect)

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

    def gravity(self, GRAVITY):
        self.y_vel += GRAVITY
        self.rect.y += self.y_vel

    def jump(self, JUMP_SPEED):
        self.y_vel = -JUMP_SPEED

    def shoot(self, BULLET, BULLET_COOLDOWN ):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_shot > BULLET_COOLDOWN:
            bullet_x = self.rect.centerx
            bullet_y = self.rect.centery


            new_bullet = BULLET(bullet_x, bullet_y, self.bullet_w, self.bullet_h, self.direction, self.player_number)
            self.bullets.append(new_bullet)
            self.last_shot = current_time

    def check_inside_block(self, blocks):
        self.inside_block = False

        for block in blocks:
            if (self.rect.colliderect(block.rect)
                    and self.rect.top > block.rect.top
                    and self.rect.left < block.rect.right
                    and self.rect.right > block.rect.left
                    and self.height < 50
            ):
                self.inside_block = True

    def collide_vertical(self, blocks):
        self.touching_ground = False

        for block in blocks:

            if (self.rect.colliderect(block.rect)
                    and self.dodge_ground == False
                    and self.inside_block == False
                    and self.rect.bottom <= block.rect.centery
                    and self.y_vel > 0):
                        self.rect.bottom = block.rect.top
                        self.touching_ground = True
                        self.jump_count = 0
                        self.y_vel = 0

    def stop_dodge(self, blocks):
        for block in blocks:
            if (self.dodge_ground == True
                    and self.rect.colliderect(block.rect)
                    and self.rect.bottom < block.rect.bottom
                    and self.rect.bottom > block.rect.centery

            ):
                self.dodge_ground = False



    def collide_border(self, SCREEN_W):
        if self.rect.centerx > SCREEN_W:
            self.rect.centerx = 0
        if self.rect.centerx < 0:
            self.rect.centerx = SCREEN_W

    def collide_bottom(self, SCREEN_H):
        if self.rect.centery > SCREEN_H:
            self.rect.centery = 0
        if self.rect.centery < 0:
            self.rect.centery = SCREEN_H

    def update(self, GRAVITY, blocks, screen, player_1, player_2, SCREEN_W, SCREEN_H):
        self.gravity(GRAVITY)
        self.check_inside_block(blocks)
        self.collide_vertical(blocks)
        self.stop_dodge(blocks)
        for bullet in self.bullets:
            bullet.update(screen, player_1, player_2)
        self.collide_border(SCREEN_W)
        self.collide_bottom(SCREEN_H)
        self.handle_move()
        # self.collide_horizontal(blocks)


