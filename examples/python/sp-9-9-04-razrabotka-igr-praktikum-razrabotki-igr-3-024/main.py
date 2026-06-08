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

    def update(self, dt, field):
        self.rect.x += int(self.vx * dt)
        self.rect.y += int(self.vy * dt)

        if self.rect.top <= field.top:
            self.rect.top = field.top
            self.vy = abs(self.vy)
        elif self.rect.bottom >= field.bottom:
            self.rect.bottom = field.bottom
            self.vy = -abs(self.vy)

    def collide_paddle(self, paddle):
        if not self.rect.colliderect(paddle.rect):
            return False

        approaching = (self.vx > 0 and paddle.rect.centerx > S.MARGIN + S.FIELD_W // 2) or (
            self.vx < 0 and paddle.rect.centerx < S.MARGIN + S.FIELD_W // 2
        )
        if not approaching:
            return False

        half = paddle.rect.height / 2
        relative_hit = (self.rect.centery - paddle.rect.centery) / half
        relative_hit = max(-1.0, min(1.0, relative_hit))

        self.vy = S.BALL_SPEED * relative_hit * 0.85
        self.vx = -self.vx

        speed = (self.vx ** 2 + self.vy ** 2) ** 0.5
        if speed > 0:
            scale = min(S.BALL_SPEED * 1.15, speed) / speed
            self.vx *= scale
            self.vy *= scale

        if self.vx > 0:
            self.rect.left = paddle.rect.right
        else:
            self.rect.right = paddle.rect.left
        return True

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=2)
