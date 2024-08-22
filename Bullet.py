import pygame


class BULLET:
    COLOR = pygame.Color("black")
    SPEED = 10

    # WIDTH, HEIGHT = 10, 5

    def __init__(self, x, y, w, h, direction, player_number):
        self.rect = pygame.Rect(x, y, w, h)
        self.direction = direction
        self.bullet_number = player_number
        self.collided = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.COLOR, self.rect)

    def collide_player(self, player_1, player_2):
        if self.rect.colliderect(player_1.rect) and self.bullet_number == 2:
            self.collided = True
            player_1.lives -= 1
        if self.rect.colliderect(player_2.rect) and self.bullet_number == 1:
            self.collided = True
            player_2.lives -= 1

    def update(self, screen, player_1, player_2):
        if not self.collided:
            if self.direction == "right":
                self.rect.x += self.SPEED
            elif self.direction == "left":
                self.rect.x -= self.SPEED
            self.draw(screen)
            self.collide_player(player_1, player_2)
