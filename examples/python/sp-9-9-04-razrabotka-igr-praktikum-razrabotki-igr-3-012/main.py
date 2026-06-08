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
