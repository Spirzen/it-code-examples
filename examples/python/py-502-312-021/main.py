
import pygame
import sys

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Размеры "мира" (больше экрана)
WORLD_WIDTH = 2000
WORLD_HEIGHT = 2000

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=(100, 100)) # Начальная позиция в мире
        self.speed = 5
        self.keys_pressed = {'w': False, 'a': False, 's': False, 'd': False}

    def update(self):
        if self.keys_pressed['w'] and self.rect.top > 0: self.rect.y -= self.speed
        if self.keys_pressed['s'] and self.rect.bottom < WORLD_HEIGHT: self.rect.y += self.speed
        if self.keys_pressed['a'] and self.rect.left > 0: self.rect.x -= self.speed
        if self.keys_pressed['d'] and self.rect.right < WORLD_WIDTH: self.rect.x += self.speed

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        """Применяет смещение камеры к сущности."""
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        """Центрирует камеру на цели."""
        x = -target.rect.centerx + int(SCREEN_WIDTH / 2)
        y = -target.rect.centery + int(SCREEN_HEIGHT / 2)
        
        # Ограничиваем камеру границами мира (чтобы не видеть пустоту за краями)
        x = min(0, max(-(self.width - SCREEN_WIDTH), x))
        y = min(0, max(-(self.height - SCREEN_HEIGHT), y))
        
        self.camera.topleft = x, y

def main():
    all_sprites = pygame.sprite.Group()
    
    player = Player()
    all_sprites.add(player)
    
    # Создадим несколько объектов для проверки работы камеры
    for i in range(5):
        obs = pygame.sprite.Sprite()
        obs.image = pygame.Surface((40, 40))
        obs.image.fill((255, 165, 0))
        obs.rect = obs.image.get_rect(center=(500 + i * 300, 500))
        all_sprites.add(obs)

    camera = Camera(WORLD_WIDTH, WORLD_HEIGHT)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                key_map = {pygame.K_w: 'w', pygame.K_a: 'a', pygame.K_s: 's', pygame.K_d: 'd'}
                if event.key in key_map: player.keys_pressed[key_map[event.key]] = True
            elif event.type == pygame.KEYUP:
                key_map = {pygame.K_w: 'w', pygame.K_a: 'a', pygame.K_s: 's', pygame.K_d: 'd'}
                if event.key in key_map: player.keys_pressed[key_map[event.key]] = False

        player.update()
        camera.update(player)

        screen.fill((30, 30, 30))
        
        # Рисуем все спрайты с учетом смещения камеры
        for sprite in all_sprites:
            screen.blit(sprite.image, camera.apply(sprite).rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
