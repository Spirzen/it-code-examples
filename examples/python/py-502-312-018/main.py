
import pygame
import sys

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((0, 255, 0)) # Зеленый
        self.rect = self.image.get_rect(center=(400, 300))
        self.speed = 5
        self.keys_pressed = {'w': False, 'a': False, 's': False, 'd': False}

    def update(self):
        if self.keys_pressed['w'] and self.rect.top > 0: self.rect.y -= self.speed
        if self.keys_pressed['s'] and self.rect.bottom < SCREEN_HEIGHT: self.rect.y += self.speed
        if self.keys_pressed['a'] and self.rect.left > 0: self.rect.x -= self.speed
        if self.keys_pressed['d'] and self.rect.right < SCREEN_WIDTH: self.rect.x += self.speed

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.image = pygame.Surface((w, h))
        self.image.fill((255, 0, 0)) # Красный
        self.rect = self.image.get_rect(topleft=(x, y))

def main():
    all_sprites = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()
    
    player = Player()
    all_sprites.add(player)
    
    # Создаем препятствия
    for i in range(5):
        obs = Obstacle(100 + i * 120, 100, 50, 50)
        all_sprites.add(obs)
        obstacles.add(obs)

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

        # Проверка столкновений
        hits = pygame.sprite.spritecollide(player, obstacles, False)
        
        if hits:
            # Если столкнулись — останавливаемся или отменяем движение
            # Вариант 1: Просто выводим сообщение (не меняя позицию)
            print("Коллизия обнаружена!")
            # Вариант 2: Откат позиции (более сложный, требует сохранения координат до движения)
            # Для простого примера остановим игрока на месте, если он пытается войти в стену
            # Здесь мы просто не будем менять логику движения, но визуально можно подсветить игрока
            
        screen.fill((30, 30, 30))
        all_sprites.draw(screen)
        
        # Визуализация коллизии (красная рамка вокруг игрока при ударе)
        if hits:
            pygame.draw.rect(screen, (255, 255, 0), player.rect, 3)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
