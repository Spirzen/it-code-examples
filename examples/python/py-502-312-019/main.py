
import pygame
import random
import math

# ... (код инициализации и класса Player из предыдущего примера можно скопировать сюда) ...

class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, color, speed_range, size_range):
        super().__init__()
        self.size = random.randint(size_range[0], size_range[1])
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        
        # Случайное направление разлета
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(speed_range[0], speed_range[1])
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        
        self.life = 1.0 # Жизнь частицы от 1.0 до 0.0
        self.decay = random.uniform(0.02, 0.05) # Скорость затухания

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        self.life -= self.decay
        
        # Уменьшаем размер по мере жизни
        new_size = int(self.size * self.life)
        if new_size <= 0:
            self.kill() # Удаляем спрайт из всех групп
        else:
            self.image = pygame.Surface((new_size, new_size))
            self.image.fill((255, 255, 255)) # Можно сделать цветным, используя alpha
            # Для простоты оставим белый, но в реальном проекте лучше использовать Surface.set_alpha
            self.rect.center = (self.rect.x + self.vx, self.rect.y + self.vy) # Корректировка центра

def create_explosion(x, y, count=20):
    particles = []
    colors = [(255, 165, 0), (255, 0, 0), (255, 255, 0)]
    for _ in range(count):
        p = Particle(x, y, random.choice(colors), (2, 5), (3, 8))
        particles.append(p)
    return particles

# Пример использования внутри цикла main —
# При клике мыши создаем частицы
# mouse_buttons = pygame.mouse.get_pressed()
# if mouse_buttons[0] —# ЛКМ
#     mx, my = pygame.mouse.get_pos()
#     explosion = create_explosion(mx, my)
#     all_sprites.add(explosion)
