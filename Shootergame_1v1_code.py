import pygame
import random

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

class PLAYER:

    def __init__(self, player_number, x, y):
        width, height = 50, 50
        self.rect = pygame.Rect(x, y, width, height)
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

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

    def check_keys(self):
        keys = pygame.key.get_pressed()
    # P1
        if self.player_number == 1:
            if keys[pygame.K_LEFT]:
                self.move_left()

            if keys[pygame.K_RIGHT]:
                self.move_right()

            if keys[pygame.K_UP]:
                if self.jump_pressed == False and self.jump_count < JUMP_LIMIT:
                    self.jump()
                    self.jump_count += 1
                    self.jump_pressed = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.jump_pressed = False

            if keys[pygame.K_SPACE]:
                self.shoot()

    # P2
        if self.player_number == 2:
            if keys[pygame.K_a]:
                self.move_left()

            if keys[pygame.K_d]:
                self.move_right()

            if keys[pygame.K_w]:
                if self.jump_pressed == False and self.jump_count < JUMP_LIMIT:
                    self.jump()
                    self.jump_count += 1
                    self.jump_pressed = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.jump_pressed = False

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

    # def dodge(self):
    #     self.y_vel += DODGE_SPEED

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
            if self.rect.colliderect(block.rect):
                    if self.rect.bottom <= block.rect.centery:
                        if self.y_vel > 0:
                            self.rect.bottom = block.rect.top
                            self.touching_ground = True
                            self.jump_count = 0
                            self.y_vel = 0

    def check_lives(self):
        global WINNER
        if self.lives < 1:
            if self.player_number == 1:
                WINNER = 2
            if self.player_number == 2:
                WINNER = 1
            main.game_over()


    def update(self):
        self.check_keys()
        self.gravity()
        self.collide_vertical(blocks)
        for bullet in self.bullets:
            bullet.update()
        self.check_lives()

class BULLET:
    COLOR = pygame.Color("black")
    SPEED = 10
    WIDTH, HEIGHT = 10, 5

    def __init__(self, x, y, direction, player_number):
        self.rect = pygame.Rect(x, y, self.WIDTH, self.HEIGHT)
        self.direction = direction
        self.bullet_number = player_number
        self.collided = False

    def draw(self):
        pygame.draw.rect(screen, self.COLOR, self.rect)




    def collide_player(self, player_1, player_2):
        if self.rect.colliderect(player_1.rect) and self.bullet_number == 2:
            self.collided = True
            player_1.lives -= 1
        if self.rect.colliderect(player_2.rect) and self.bullet_number == 1:
            self.collided = True
            player_2.lives -= 1

    def update(self):
        if self.collided == False:
            if self.direction == "right":
                self.rect.x += self.SPEED
            elif self.direction == "left":
                self.rect.x -= self.SPEED
            self.draw()
            self.collide_player(player_1, player_2)

class BLOCK:
    COLOR = pygame.Color("dark green")
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        pygame.draw.rect(screen, self.COLOR, self.rect)

class RANDOM_MAP:

    def __init__(self, blocks):

        for col in range(SCREEN_H // BLOCK_H):
            if col % random.randint(3, 4) == 0:
                for row in range(SCREEN_W // BLOCK_W):
                    if row % random.randint(5, 6) == 0:
                        blocks.append(BLOCK(row * BLOCK_H, col * BLOCK_H, random.randint(1, 5) * BLOCK_W, BLOCK_H))



class MAIN:
    def __init__(self):
        self.lives_font = pygame.font.SysFont("Arial", 30)
        self.title_font = pygame.font.SysFont("Arial", 50, True)
        self.subtitle_font = pygame.font.SysFont("Arial", 30)

    def draw_text(self, text, font, color, center_x, center_y):
        text_img = font.render(text, True, color)
        text_rect = text_img.get_rect(center=(center_x, center_y))
        screen.blit(text_img, text_rect)

    def game_over(self):
        screen.fill((0,0,0))
        if WINNER == 1:
            game_over_color = pygame.Color("red")
        elif WINNER == 2:
            game_over_color = pygame.Color("blue")

        self.draw_text("GAME OVER", self.title_font, game_over_color, SCREEN_W // 2, SCREEN_H // 2)
        self.draw_text(f"Player {WINNER} wins", self.subtitle_font, game_over_color, SCREEN_W // 2, SCREEN_H // 2 + 50)


    def draw_elements(self, blocks, player_1, player_2):
        player_1.draw()
        player_2.draw()
        for block in blocks:
            block.draw()

# F-String from Vid 3
        self.draw_text(f"P1: {player_1.lives}", self.lives_font, (255, 255, 255), SCREEN_W - 100, 50)
        self.draw_text(f"P2: {player_2.lives}", self.lives_font, (255, 255, 255), 100, 50)


# INSTANZEN
main = MAIN()
player_1 = PLAYER(1, 500, 0)
player_2 = PLAYER(2, 200, 0)
blocks = [
    BLOCK(0, SCREEN_H - BLOCK_H, SCREEN_W, BLOCK_H)
]
bullet = BULLET
rand_map = RANDOM_MAP(blocks)


# GAME LOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.Color("light blue"))

    main.draw_elements(blocks, player_1, player_2)
    player_1.update()
    player_2.update()

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()