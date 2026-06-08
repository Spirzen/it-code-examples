class AnimatedPlayer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.frames = []
        for i in range(4):
            img = pygame.image.load(f"player_{i}.png").convert_alpha()
            self.frames.append(img)
        self.image = self.frames[0]
        self.rect = self.image.get_rect()
        self.frame_index = 0
        self.last_update = 0
        self.frame_rate = 100  # мс между кадрами

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.image = self.frames[self.frame_index]
