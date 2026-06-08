class Ball:
    def __init__(self):
        cx = S.MARGIN + S.FIELD_W // 2
        cy = S.MARGIN + S.FIELD_H // 2
        self.rect = pygame.Rect(0, 0, S.BALL_SIZE, S.BALL_SIZE)
        self.rect.center = (cx, cy)
        self.vx = 0.0
        self.vy = 0.0
        self.color = S.COLOR_BALL

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=2)


ball = Ball()
