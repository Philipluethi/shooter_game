import pygame

pygame.init()

WIDTH, HEIGHT = 1000, 500
FPS = 60
GRAVITY = 1
JUMP_SPEED = 15
BULLET_COOLDOWN = 1000 / 5

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.update()
pygame.display.set_caption("Shooter Game 1v1")

class BLOCK:
    COLOR = pygame.Color("dark green")
    def __init__(self, x, y, width, height):
        self.block_rect = pygame.Rect(x, y, width, height)

    def draw(self):
        pygame.draw.rect(screen, self.COLOR, self.block_rect)

class PLAYER:
    COLOR = pygame.Color("red")

    def __init__(self, player_number, x, y):
        width, height = 50, 50
        self.rect = pygame.Rect(x, y, width, height)
        self.direction = "right"
        self.x_vel = 5
        self.y_vel = 0
        self.jump_count = 0
        self.bullets = []
        self.last_shot = pygame.time.get_ticks()
        self.player_number = player_number


    def draw(self):
        pygame.draw.rect(screen, self.COLOR, self.rect)

    def check_keys(self):
        keys = pygame.key.get_pressed()
        if self.player_number == 1:
            if keys[pygame.K_LEFT]:
                self.move_left()
            if keys[pygame.K_RIGHT]:
                self.move_right()
            if keys[pygame.K_UP] and self.jump_count < 1:
                self.jump()
            if keys[pygame.K_SPACE]:
                self.shoot()
        if self.player_number == 2:
            if keys[pygame.K_a]:
                self.move_left()
            if keys[pygame.K_d]:
                self.move_right()
            if keys[pygame.K_w] and self.jump_count < 1:
                self.jump()
            if keys[pygame.K_CAPSLOCK]:
                self.shoot()

    def move_left(self):
        self.rect.x -= self.x_vel
        self.direction = "left"

    def move_right(self):
        self.rect.x += self.x_vel
        self.direction = "right"

    def gravity(self):
        self.y_vel += GRAVITY
        self.rect.y += self.y_vel

    def jump(self):
        self.y_vel = -JUMP_SPEED
        self.jump_count += 1

    def shoot(self):
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
            if self.rect.colliderect(block.block_rect):
                if self.y_vel > 0:
                    self.rect.bottom = block.block_rect.top
                    self.y_vel = 0
                    self.touching_ground = True
                    self.jump_count = 0

    def collide_horizontal(self, blocks):
        for block in blocks:
            if self.rect.colliderect(block.block_rect) and self.rect.bottom != block.block_rect.top and self.x_vel != 0:
                if self.rect.right > block.block_rect.left and self.rect.left < block.block_rect.left:
                    self.rect.right = block.block_rect.left
                elif self.rect.left < block.block_rect.right and self.rect.right > block.block_rect.right:
                    self.rect.left = block.block_rect.right

    def update(self):
        self.check_keys()
        self.gravity()
        self.collide_vertical(blocks)
        self.collide_horizontal(blocks)
        for bullet in self.bullets:
            bullet.update()


class BULLET:
    COLOR = pygame.Color("yellow")
    SPEED = 10
    WIDTH, HEIGHT = 10, 5

    def __init__(self, x, y, direction, player_number):
        self.rect = pygame.Rect(x, y, self.WIDTH, self.HEIGHT)
        self.direction = direction
        self.bullet_number = player_number
        self.collided = False

    def draw(self):
        pygame.draw.rect(screen, self.COLOR, self.rect)

    def update(self):
        if self.collided == False:
            if self.direction == "right":
                self.rect.x += self.SPEED
            elif self.direction == "left":
                self.rect.x -= self.SPEED
            self.draw()
            self.collide_player(player_1, player_2)


    def collide_player(self, player_1, player_2):
        if self.rect.colliderect(player_1.rect) and self.bullet_number == 2:
            self.collided = True
        if self.rect.colliderect(player_2.rect) and self.bullet_number == 1:
            self.collided = True


def draw_elements(blocks, player_1, player_2):
    player_1.draw()
    player_2.draw()
    for block in blocks:
        block.draw()

player_1 = PLAYER(1, 500, 0)
player_2 = PLAYER(2, 200, 0)

blocks = [
    BLOCK(200, 450, 500, 50),
    BLOCK(300, 350, 200, 50)
]
bullet = BULLET


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.Color("light blue"))

    draw_elements(blocks, player_1, player_2)
    player_1.update()
    player_2.update()

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()