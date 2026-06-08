class ChasingEnemy(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=(100, 100))
        self.player = player
        self.speed = 3

    def update(self):
        if self.rect.centerx < self.player.rect.centerx:
            self.rect.x += self.speed
        elif self.rect.centerx > self.player.rect.centerx:
            self.rect.x -= self.speed
        if self.rect.centery < self.player.rect.centery:
            self.rect.y += self.speed
        elif self.rect.centery > self.player.rect.centery:
            self.rect.y -= self.speed
