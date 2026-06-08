
import pygame
import sys

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Состояния игры
STATE_PLAYING = "playing"
STATE_PAUSED = "paused"
STATE_GAME_OVER = "game_over"

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=(400, 300))
        self.hp = 100
        self.speed = 5
        self.keys_pressed = {'w': False, 'a': False, 's': False, 'd': False}

    def update(self):
        if not self.keys_pressed['w'] and not self.keys_pressed['a'] and \
           not self.keys_pressed['s'] and not self.keys_pressed['d']:
            return # Нет движения
            
        if self.keys_pressed['w'] and self.rect.top > 0: self.rect.y -= self.speed
        if self.keys_pressed['s'] and self.rect.bottom < SCREEN_HEIGHT: self.rect.y += self.speed
        if self.keys_pressed['a'] and self.rect.left > 0: self.rect.x -= self.speed
        if self.keys_pressed['d'] and self.rect.right < SCREEN_WIDTH: self.rect.x += self.speed

def draw_text(surface, text, size, color, x, y, center=False):
    font = pygame.font.SysFont('Arial', size)
    text_surface = font.render(text, True, color)
    rect = text_surface.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    surface.blit(text_surface, rect)

def main():
    player = Player()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    
    game_state = STATE_PLAYING
    
    running = True
    keys_pressed = {'w': False, 'a': False, 's': False, 'd': False}

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if game_state == STATE_PLAYING:
                        game_state = STATE_PAUSED
                    elif game_state == STATE_PAUSED:
                        game_state = STATE_PLAYING
                
                elif event.key == pygame.K_r and game_state == STATE_GAME_OVER:
                    # Перезапуск
                    player.hp = 100
                    player.rect.center = (400, 300)
                    game_state = STATE_PLAYING

                key_map = {pygame.K_w: 'w', pygame.K_a: 'a', pygame.K_s: 's', pygame.K_d: 'd'}
                if event.key in key_map: keys_pressed[key_map[event.key]] = True

            elif event.type == pygame.KEYUP:
                key_map = {pygame.K_w: 'w', pygame.K_a: 'a', pygame.K_s: 's', pygame.K_d: 'd'}
                if event.key in key_map: keys_pressed[key_map[event.key]] = False
        
        # Логика зависит от состояния
        if game_state == STATE_PLAYING:
            player.update()
            
            # Имитация получения урона (для примера - случайный удар раз в секунду)
            import random
            if random.random() < 0.02: # 2% шанс в кадр
                player.hp -= 10
                if player.hp <= 0:
                    game_state = STATE_GAME_OVER

        elif game_state == STATE_PAUSED:
            pass # Логика игры не обновляется

        # Отрисовка
        screen.fill((30, 30, 30))
        
        if game_state == STATE_PLAYING or game_state == STATE_PAUSED:
            all_sprites.draw(screen)
            # Рисуем здоровье
            draw_text(screen, f"HP: {player.hp}", 24, (255, 255, 255), 20, 20)
        
        if game_state == STATE_PAUSED:
            # Затемнение фона
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            overlay.set_alpha(128)
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))
            draw_text(screen, "ПАУЗА", 60, (255, 255, 255), SCREEN_WIDTH//2, SCREEN_HEIGHT//2, center=True)
            draw_text(screen, "Нажмите ESC для продолжения", 20, (200, 200, 200), SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 50, center=True)

        if game_state == STATE_GAME_OVER:
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            overlay.set_alpha(200)
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))
            draw_text(screen, "GAME OVER", 60, (255, 0, 0), SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 50, center=True)
            draw_text(screen, "Нажмите R для рестарта", 24, (255, 255, 255), SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 50, center=True)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
