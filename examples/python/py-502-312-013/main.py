class Bonus(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 800)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = 3

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > 600:
            self.kill()

# В главном цикле
hits = pygame.sprite.spritecollide(player, bonuses, True)  # True удаляет бонус
for hit in hits:
    score += 10
