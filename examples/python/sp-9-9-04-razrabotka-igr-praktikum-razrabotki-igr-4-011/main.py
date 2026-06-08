def collide_with(self, other):
    r1 = pygame.Rect(0, 0, self.width, self.height)
    r1.center = (int(self.x), int(self.y))
    r2 = pygame.Rect(0, 0, other.width, other.height)
    r2.center = (int(other.x), int(other.y))
    if r1.colliderect(r2):
        dx = self.x - other.x
        dy = self.y - other.y
        if dx == 0 and dy == 0:
            dx = 1
        length = math.hypot(dx, dy)
        push = 3.0
        self.x += (dx / length) * push
        self.y += (dy / length) * push
        self.speed *= 0.85
        other.speed *= 0.85
