import pygame
import settings as S


class Paddle:
    def __init__(self, x, color):
        y = S.MARGIN + (S.FIELD_H - S.PADDLE_H) // 2
        self.rect = pygame.Rect(x, y, S.PADDLE_W, S.PADDLE_H)
        self.color = color
        self.speed = S.PADDLE_SPEED

    def move(self, direction, dt):
        dy = direction * self.speed * dt
        self.rect.y += int(dy)
        top = S.MARGIN
        bottom = S.MARGIN + S.FIELD_H - self.rect.height
        self.rect.top = max(top, min(bottom, self.rect.top))

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=3)
