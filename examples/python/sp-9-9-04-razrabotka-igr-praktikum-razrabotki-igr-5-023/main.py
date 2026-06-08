# В Game
self.lock_timer = 0.0
self.on_ground = False

def _on_gravity_step(self, moved_down):
    if moved_down:
        self.on_ground = False
        self.lock_timer = 0.0
        return False
    if not self.on_ground:
        self.on_ground = True
        self.lock_timer = 0.0
    self.lock_timer += dt
    if self.lock_timer >= S.LOCK_DELAY:
        self._lock_current()
        return True
    return False
