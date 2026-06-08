class PhysicsPlayer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = 0
        self.accel_x = 0
        self.accel_y = 0
        self.friction = -0.1

    def update(self):
        self.accel_x = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.accel_x = -0.5
        if keys[pygame.K_RIGHT]:
            self.accel_x = 0.5
        
        self.accel_x += self.vel_x * self.friction
        self.vel_x += self.accel_x
        self.rect.x += self.vel_x
        
        # Ограничение скорости
        if self.vel_x > 10: self.vel_x = 10
        if self.vel_x < -10: self.vel_x = -10
