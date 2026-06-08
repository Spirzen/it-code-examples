import pygame
import settings as S


class Ball:
    def __init__(self):
        self.reset(center=True)
        self.color = S.COLOR_BALL

    def reset(self, center=False, direction=1):
        cx = S.MARGIN + S.FIELD_W // 2
        cy = S.MARGIN + S.FIELD_H // 2
        self.rect = pygame.Rect(0, 0, S.BALL_SIZE, S.BALL_SIZE)
        self.rect.center = (cx, cy)
        if center:
            self.vx = 0.0
            self.vy = 0.0
        else:
            self.vx = S.BALL_SPEED * direction
            self.vy = S.BALL_SPEED * 0.35

    def update(self, dt):
        self.rect.x += int(self.vx * dt)
        self.rect.y += int(self.vy * dt)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=2)
