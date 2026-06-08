
import pygame
import sys
import json
import os

SAVE_FILE = "save_game.json"

# ... (код инициализации Pygame и класса Player из предыдущих примеров) ...

class SaveablePlayer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=(400, 300))
        self.hp = 100
        self.level = 1
        self.score = 0

    def save_data(self):
        """Создает словарь данных для сохранения"""
        return {
            "position": {"x": self.rect.centerx, "y": self.rect.centery},
            "hp": self.hp,
            "level": self.level,
            "score": self.score
        }

    def load_data(self, Данные):
        """Загружает данные из словаря"""
        if "position" in Данные:
            self.rect.centerx = Данные["position"]["x"]
            self.rect.centery = Данные["position"]["y"]
        if "hp" in Данные:
            self.hp = Данные["hp"]
        if "level" in Данные:
            self.level = Данные["level"]
        if "score" in Данные:
            self.score = Данные["score"]

def save_game(player):
    try:
        data = player.save_data()
        with open(SAVE_FILE, 'w', encoding='utf-8') as f:
            json.dump(Данные, f, indent=4, ensure_ascii=False)
        print("Игра сохранена успешно.")
    except Exception as e:
        print(f"Ошибка сохранения: {e}")

def load_game(player):
    if not os.path.exists(SAVE_FILE):
        print("Файл сохранения не найден.")
        return False
    
    try:
        with open(SAVE_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        player.load_data(Данные)
        print("Игра загружена.")
        return True
    except Exception as e:
        print(f"Ошибка загрузки: {e}")
        return False

def main():
    player = SaveablePlayer()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    
    # Проверка наличия сохранения при старте
    # Если хотите всегда начинать заново, закомментируйте строку ниже
    # load_game(player) 

    running = True
    keys_pressed = {'w': False, 'a': False, 's': False, 'd': False}

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F5:
                    save_game(player)
                
                key_map = {pygame.K_w: 'w', pygame.K_a: 'a', pygame.K_s: 's', pygame.K_d: 'd'}
                if event.key in key_map: keys_pressed[key_map[event.key]] = True

            elif event.type == pygame.KEYUP:
                key_map = {pygame.K_w: 'w', pygame.K_a: 'a', pygame.K_s: 's', pygame.K_d: 'd'}
                if event.key in key_map: keys_pressed[key_map[event.key]] = False
        
        # Обновление логики
        speed = 5
        if keys_pressed['w'] and player.rect.top > 0: player.rect.y -= speed
        if keys_pressed['s'] and player.rect.bottom < SCREEN_HEIGHT: player.rect.y += speed
        if keys_pressed['a'] and player.rect.left > 0: player.rect.x -= speed
        if keys_pressed['d'] and player.rect.right < SCREEN_WIDTH: player.rect.x += speed
        
        # Пример изменения данных
        player.score += 1

        # Отрисовка
        screen.fill((30, 30, 30))
        all_sprites.draw(screen)
        
        font = pygame.font.SysFont('Arial', 20)
        info_text = f"Score: {player.score} | F5: Save"
        screen.blit(font.render(info_text, True, (255, 255, 255)), (20, 20))

        pygame.display.flip()
        clock.tick(60)

    # Автоматическое сохранение при выходе
    save_game(player)
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
