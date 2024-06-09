import pygame

pygame.init()

WIDTH, HEIGHT = 1000, 500
FPS = 60
GRAVITY = 1

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

    def __init__(self, x, y, width, height):
        self.player_rect = pygame.Rect(x, y, width, height)
        self.direction = "right"
        self.x_vel = 5
        self.y_vel = 0

    def draw(self):
        pygame.draw.rect(screen, self.COLOR, self.player_rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player_rect.x -= self.x_vel
        if keys[pygame.K_RIGHT]:
            self.player_rect.x += self.x_vel

        self.y_vel += GRAVITY
        self.player_rect.y += self.y_vel

    def collide_floor(self, blocks):
        for block in blocks:
            if self.player_rect.colliderect(block.block_rect):
                if self.y_vel > 0:
                    self.player_rect.bottom = block.block_rect.top
                    self.y_vel = 0


def draw_elements(blocks, player):
    player.draw()
    for block in blocks:
        block.draw()

player = PLAYER(300, 0, 50, 50)
blocks = [
    BLOCK(200, 450, 500, 50),
    BLOCK(200, 200, 500, 50)
]
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(pygame.Color("light blue"))
    draw_elements(blocks, player)

    player.move()
    player.collide_floor(blocks)

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()