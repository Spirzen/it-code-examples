
import pygame
import sys

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

class HealthPlayer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 255, 0)) # Зеленый
        self.original_color = (0, 255, 0)
        self.rect = self.image.get_rect(center=(400, 300))
        
        self.hp = 100
        self.max_hp = 100
        self.is_hit = False
        self.hit_timer = 0
        self.hit_duration = 10 # Кадров (около 0.16 сек при 60 FPS)

    def take_damage(self, amount):
        """Получение урона"""
        self.hp -= amount
        if self.hp < 0: self.hp = 0
        
        # Включаем эффект удара
        self.is_hit = True
        self.hit_timer = self.hit_duration

    def update(self):
        if self.is_hit:
            self.hit_timer -= 1
            # Мигаем: каждый четный кадр меняем цвет на белый, нечетный - красный
            if self.hit_timer % 2 == 0:
                self.image.fill((255, 255, 255)) # Белый
            else:
                self.image.fill((255, 0, 0))     # Красный
            
            if self.hit_timer <= 0:
                self.is_hit = False
                self.image.fill(self.original_color)
        else:
            # Если есть движение (упрощено), можно добавить анимацию, но здесь только удар
            pass

def main():
    player = HealthPlayer()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    
    running = True
    mouse_buttons = [False, False, False]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Клик мышью наносит урон игроку (для теста)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # ЛКМ
                    player.take_damage(20)

        player.update()

        screen.fill((40, 40, 40))
        all_sprites.draw(screen)
        
        # Отображение полоски здоровья
        bar_width = 200
        bar_height = 20
        bar_x = 50
        bar_y = 50
        
        # Фон полоски
        pygame.draw.rect(screen, (100, 100, 100), (bar_x, bar_y, bar_width, bar_height))
        # Текущее здоровье
        hp_width = int(bar_width * (player.hp / player.max_hp))
        hp_color = (0, 255, 0) if player.hp > 30 else (255, 0, 0)
        pygame.draw.rect(screen, hp_color, (bar_x, bar_y, hp_width, bar_height))
        
        # Текст
        font = pygame.font.SysFont('Arial', 16)
        text = font.render(f"HP: {player.hp}/{player.max_hp}", True, (255, 255, 255))
        screen.blit(text, (bar_x, bar_y - 20))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
