import pygame

class PLAYER:

    def __init__(self, player_number, x, y):
        self.width, self.height = 40, 40
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.direction = "right"
        self.x_vel = 5
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

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move_left(self):
        self.rect.x -= self.x_vel
        self.direction = "left"

    def move_right(self):
        self.rect.x += self.x_vel
        self.direction = "right"

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
            new_bullet = BULLET(bullet_x, bullet_y, self.direction, self.player_number)
            self.bullets.append(new_bullet)
            self.last_shot = current_time


    def collide_vertical(self, blocks):
        self.touching_ground = False

        for block in blocks:
            if self.rect.colliderect(block.rect):
                    if self.rect.bottom <= block.rect.centery:
                        if self.y_vel > 0:
                            self.rect.bottom = block.rect.top
                            self.touching_ground = True
                            self.jump_count = 0
                            self.y_vel = 0

    def collide_border(self, SCREEN_W):
        if self.rect.centerx > SCREEN_W:
            self.rect.centerx = 0
            print("colided right")
        if self.rect.centerx < 0:
            self.rect.centerx = SCREEN_W
            print("colided left")


    def update(self, GRAVITY, blocks, screen, player_1, player_2, SCREEN_W):
        self.gravity(GRAVITY)
        self.collide_vertical(blocks)
        for bullet in self.bullets:
            bullet.update(screen, player_1, player_2)
        self.collide_border(SCREEN_W)
