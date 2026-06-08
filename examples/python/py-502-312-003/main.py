
import pygame
import sys

# Инициализация Pygame
pygame.init()

# Константы конфигурации
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
SPEED = 5

# Цвета (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Настройка экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("WASD Movement Example")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Создаем спрайт: можно использовать surface или rect
        self.image = pygame.Surface((40, 40))
        self.image.fill(RED)
        
        # Получаем прямоугольник вокруг изображения
        self.rect = self.image.get_rect()
        
        # Начальная позиция (центр экрана)
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.centery = SCREEN_HEIGHT // 2
        
        # Словарь для хранения состояния клавиш
        self.keys_pressed = {
            'w': False,
            'a': False,
            's': False,
            'd': False
        }

    def update(self):
        # Проверка нажатых клавиш
        if self.keys_pressed['w'] and self.rect.top > 0:
            self.rect.y -= SPEED
        if self.keys_pressed['s'] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += SPEED
        if self.keys_pressed['a'] and self.rect.left > 0:
            self.rect.x -= SPEED
        if self.keys_pressed['d'] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += SPEED

def main():
    all_sprites = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)

    running = True
    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Отслеживание нажатия клавиш
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.keys_pressed['w'] = True
                elif event.key == pygame.K_a:
                    player.keys_pressed['a'] = True
                elif event.key == pygame.K_s:
                    player.keys_pressed['s'] = True
                elif event.key == pygame.K_d:
                    player.keys_pressed['d'] = True
            
            # Отслеживание отпускания клавиш
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player.keys_pressed['w'] = False
                elif event.key == pygame.K_a:
                    player.keys_pressed['a'] = False
                elif event.key == pygame.K_s:
                    player.keys_pressed['s'] = False
                elif event.key == pygame.K_d:
                    player.keys_pressed['d'] = False

        # Обновление логики
        all_sprites.update()

        # Отрисовка
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # Перерисовка экрана
        pygame.display.flip()
        
        # Ограничение FPS
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
