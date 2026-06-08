import math
import sys
import pygame
import config as C


class Car:
    def __init__(self, x, y, angle, color):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 0.0
        self.color = color
        self.width = 44
        self.height = 22

    def apply_input(self, keys):
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.speed += C.ACCELERATION
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.speed -= C.BRAKE
        self.speed *= C.FRICTION
        self.speed = max(C.MIN_SPEED, min(C.MAX_SPEED, self.speed))

    def steer(self, keys):
        if abs(self.speed) < C.STEER_MIN_SPEED:
            return
        direction = 1 if self.speed >= 0 else -1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.angle -= C.TURN_SPEED * direction
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.angle += C.TURN_SPEED * direction

    def move(self):
        rad = math.radians(self.angle)
        self.x += math.cos(rad) * self.speed
        self.y += math.sin(rad) * self.speed

    def draw(self, surface):
        body = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.rect(body, self.color, (0, 0, self.width, self.height), border_radius=4)
        pygame.draw.rect(body, (200, 220, 255), (self.width - 14, 4, 10, self.height - 8), border_radius=2)
        rotated = pygame.transform.rotate(body, -self.angle)
        rect = rotated.get_rect(center=(int(self.x), int(self.y)))
        surface.blit(rotated, rect)


def draw_track(surface):
    outer = pygame.Rect(
        C.TRACK_CX - C.OUTER_RX, C.TRACK_CY - C.OUTER_RY,
        C.OUTER_RX * 2, C.OUTER_RY * 2,
    )
    inner = pygame.Rect(
        C.TRACK_CX - C.INNER_RX, C.TRACK_CY - C.INNER_RY,
        C.INNER_RX * 2, C.INNER_RY * 2,
    )
    pygame.draw.ellipse(surface, C.COLOR_ASPHALT, outer)
    pygame.draw.ellipse(surface, C.COLOR_LAWN, inner)
    pygame.draw.ellipse(surface, C.COLOR_LINE, outer, 3)
    pygame.draw.ellipse(surface, C.COLOR_LINE, inner, 2)


pygame.init()
screen = pygame.display.set_mode((C.SCREEN_W, C.SCREEN_H))
pygame.display.set_caption("Racing — этап 5")
clock = pygame.time.Clock()

start_y = C.TRACK_CY + (C.INNER_RY + C.OUTER_RY) // 2
player = Car(C.TRACK_CX, start_y, -90, (220, 50, 50))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    keys = pygame.key.get_pressed()
    player.apply_input(keys)
    player.steer(keys)
    player.move()

    screen.fill(C.COLOR_GRASS)
    draw_track(screen)
    player.draw(screen)
    pygame.display.flip()
    clock.tick(C.FPS)

pygame.quit()
sys.exit()
