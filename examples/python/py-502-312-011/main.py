class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill((100, 100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# В цикле игрока
hits = pygame.sprite.spritecollide(player, platforms, False)
if hits:
    if player.vel_y > 0:  # Падение вниз
        player.rect.bottom = hits[0].rect.top
        player.vel_y = 0
        player.jumping = False
