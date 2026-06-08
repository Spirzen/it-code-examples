class Paddle:
    def __init__(self, x, color):
        y = S.MARGIN + (S.FIELD_H - S.PADDLE_H) // 2
        self.rect = pygame.Rect(x, y, S.PADDLE_W, S.PADDLE_H)
        self.color = color
        self.speed = S.PADDLE_SPEED

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=3)


paddle_left = Paddle(S.MARGIN + 8, S.COLOR_PADDLE_LEFT)
paddle_right = Paddle(
    S.MARGIN + S.FIELD_W - S.PADDLE_W - 8,
    S.COLOR_PADDLE_RIGHT,
)
