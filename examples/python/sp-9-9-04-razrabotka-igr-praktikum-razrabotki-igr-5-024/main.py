DAS_DELAY = 0.15   # пауза до автоповтора, сек
DAS_RATE = 0.05    # интервал повторных шагов

# В Game.__init__
self.das_timer = 0.0
self.das_dir = 0

def _update_das(self, dt):
    keys = pygame.key.get_pressed()
    want = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])
    if want == 0:
        self.das_dir = 0
        self.das_timer = 0.0
        return
    if want != self.das_dir:
        self.das_dir = want
        self.das_timer = 0.0
        self.active.try_move(self.board, want, 0)
        return
    self.das_timer += dt
    interval = DAS_DELAY if self.das_timer < DAS_DELAY else DAS_RATE
    if self.das_timer >= DAS_DELAY:
        sub = self.das_timer - DAS_DELAY
        steps = int(sub / DAS_RATE)
        if steps > 0:
            for _ in range(steps):
                if not self.active.try_move(self.board, want, 0):
                    break
            self.das_timer = DAS_DELAY + (sub % DAS_RATE)
