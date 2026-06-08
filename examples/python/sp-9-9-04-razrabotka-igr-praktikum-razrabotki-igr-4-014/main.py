import math
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

    def collide_with(self, other):
        r1 = pygame.Rect(0, 0, self.width, self.height)
        r1.center = (int(self.x), int(self.y))
        r2 = pygame.Rect(0, 0, other.width, other.height)
        r2.center = (int(other.x), int(other.y))
        if r1.colliderect(r2):
            dx = self.x - other.x
            dy = self.y - other.y
            if dx == 0 and dy == 0:
                dx = 1
            length = math.hypot(dx, dy)
            push = 3.0
            self.x += (dx / length) * push
            self.y += (dy / length) * push
            self.speed *= 0.85
            other.speed *= 0.85

    def draw(self, surface):
        body = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.rect(body, self.color, (0, 0, self.width, self.height), border_radius=4)
        pygame.draw.rect(body, (200, 220, 255), (self.width - 14, 4, 10, self.height - 8), border_radius=2)
        rotated = pygame.transform.rotate(body, -self.angle)
        rect = rotated.get_rect(center=(int(self.x), int(self.y)))
        surface.blit(rotated, rect)
