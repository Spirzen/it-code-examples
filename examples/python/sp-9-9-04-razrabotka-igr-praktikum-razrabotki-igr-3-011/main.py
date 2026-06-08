    def collide_paddle(self, paddle):
        if not self.rect.colliderect(paddle.rect):
            return False
        if self.vx > 0 and self.rect.centerx < paddle.rect.centerx:
            return False
        if self.vx < 0 and self.rect.centerx > paddle.rect.centerx:
            return False

        self.vx = -self.vx
        if self.rect.centerx < paddle.rect.centerx:
            self.rect.left = paddle.rect.left - self.rect.width
        else:
            self.rect.right = paddle.rect.right + self.rect.width
        return True
