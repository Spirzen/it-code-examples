    def update(self, dt, field, paddles=()):
        step_dt = dt / S.PHYSICS_STEPS
        for _ in range(S.PHYSICS_STEPS):
            self.rect.x += int(self.vx * step_dt)
            self.rect.y += int(self.vy * step_dt)
            self._bounce_walls(field)
            for paddle in paddles:
                self.collide_paddle(paddle)

    def _bounce_walls(self, field):
        if self.rect.top <= field.top:
            self.rect.top = field.top
            self.vy = abs(self.vy)
        elif self.rect.bottom >= field.bottom:
            self.rect.bottom = field.bottom
            self.vy = -abs(self.vy)
