
import pygame
import sys

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

class AnimatedPlayer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Имитация спрайт-листа: 4 кадра по 30px ширины, высота 30px
        # В реальности: image = pygame.image.load("walk.png")
        sheet_width = 120 # 4 кадра * 30px
        sheet_height = 30
        
        # Создаем тестовую картинку (полоски разного цвета для разных кадров)
        self.sheet = pygame.Surface((sheet_width, sheet_height))
        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
        for i, color in enumerate(colors):
            self.sheet.subsurface(pygame.Rect(i * 30, 0, 30, 30)).fill(color)

        self.frames = []
        frame_size = 30
        for i in range(len(colors)):
            # Вырезаем кадр из листа
            frame = self.sheet.subsurface(pygame.Rect(i * frame_size, 0, frame_size, frame_size)).copy()
            self.frames.append(frame)
        
        self.frame_index = 0
        self.current_frame = self.frames[self.frame_index]
        self.image = self.current_frame
        self.rect = self.image.get_rect(center=(400, 300))
        
        self.animation_speed = 0.15 # Скорость смены кадров (меньше = медленнее)
        self.timer = 0
        self.is_moving = False

    def update(self):
        # Если игрок движется, включаем анимацию
        if self.is_moving:
            self.timer += 1
            if self.timer >= 10: # Меняем кадр каждые 10 кадров (примерно 6 раз в секунду при 60 FPS)
                self.timer = 0
                self.frame_index = (self.frame_index + 1) % len(self.frames)
                self.current_frame = self.frames[self.frame_index]
                self.image = self.current_frame.copy() # Важно копировать, если меняются свойства
                self.rect.center = self.rect.center # Обновляем центр, чтобы rect не сместился
        else:
            # Статичный кадр (первый или последний)
            pass

    def set_moving(self, moving):
        self.is_moving = moving

def main():
    player = AnimatedPlayer()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    
    # Добавим простой текст для управления
    font = pygame.font.SysFont('Arial', 20)
    text = font.render("Держи W/A/S/D для движения", True, (0, 0, 0))

    running = True
    keys_pressed = {'w': False, 'a': False, 's': False, 'd': False}

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                key_map = {pygame.K_w: 'w', pygame.K_a: 'a', pygame.K_s: 's', pygame.K_d: 'd'}
                if event.key in key_map: keys_pressed[key_map[event.key]] = True
            elif event.type == pygame.KEYUP:
                key_map = {pygame.K_w: 'w', pygame.K_a: 'a', pygame.K_s: 's', pygame.K_d: 'd'}
                if event.key in key_map: keys_pressed[key_map[event.key]] = False

        # Логика движения
        speed = 5
        if keys_pressed['w']: player.rect.y -= speed
        if keys_pressed['s']: player.rect.y += speed
        if keys_pressed['a']: player.rect.x -= speed
        if keys_pressed['d']: player.rect.x += speed
        
        # Проверка: движется ли игрок?
        moved = any([keys_pressed[k] for k in keys_pressed])
        player.set_moving(moved)
        player.update()

        screen.fill((240, 240, 240))
        all_sprites.draw(screen)
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
