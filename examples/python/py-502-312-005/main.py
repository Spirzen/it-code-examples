class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, dir_x, dir_y, speed=10):
        super().__init__()
        self.image = pygame.Surface((8, 8))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.vx = dir_x * speed
        self.vy = dir_y * speed

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if not screen.get_rect().colliderect(self.rect):
            self.kill()
