class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 800)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(2, 8)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > 600:
            self.rect.x = random.randrange(0, 800)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(2, 8)
