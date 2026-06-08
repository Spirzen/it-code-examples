class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 5))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 10

    def update(self):
        self.rect.x += self.speed
        if self.rect.left > 800:
            self.kill()

# В обработчике KEYDOWN при pygame.K_SPACE —
bullet = Bullet(player.rect.centerx, player.rect.centery)
all_sprites.add(bullet)
bullets.add(bullet)
