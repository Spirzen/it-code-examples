
import pygame
import sys

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

ITEM_SIZE = 50
GRID_ROWS = 4
GRID_COLS = 5
START_X = 50
START_Y = 50

class Inventory:
    def __init__(self):
        self.slots = [None] * (GRID_ROWS * GRID_COLS)
        self.slot_rects = []
        
        # Генерируем прямоугольники слотов
        for r in range(GRID_ROWS):
            for c in range(GRID_COLS):
                rect = pygame.Rect(
                    START_X + c * (ITEM_SIZE + 5), 
                    START_Y + r * (ITEM_SIZE + 5), 
                    ITEM_SIZE, ITEM_SIZE
                )
                self.slot_rects.append(rect)

    def draw(self, surface):
        # Рисуем фон инвентаря
        pygame.draw.rect(surface, (40, 40, 40), (START_X - 5, START_Y - 5, 
                                                GRID_COLS * (ITEM_SIZE + 5) + 5, 
                                                GRID_ROWS * (ITEM_SIZE + 5) + 5), 
                        border_radius=5)
        
        # Рисуем слоты
        for i, rect in enumerate(self.slot_rects):
            color = (70, 70, 70) if self.slots[i] is None else (100, 100, 100)
            pygame.draw.rect(surface, color, rect, 2)
            
            if self.slots[i]:
                # Рисуем предмет (условно цветной квадрат)
                item_color = self.slots[i]['color']
                pygame.draw.rect(surface, item_color, rect.inflate(-4, -4))
                
                # Текст названия (опционально)
                font = pygame.font.SysFont('Arial', 10)
                text = font.render(str(i), True, (255, 255, 255))
                surface.blit(text, (rect.x + 2, rect.y + 2))

    def handle_click(self, pos):
        """Проверяет клик по слоту"""
        for i, rect in enumerate(self.slot_rects):
            if rect.collidepoint(pos):
                print(f"Клик по слоту {i}")
                # Логика: взять предмет, положить предмет и т.д.
                if self.slots[i] is None:
                    # Пример добавления предмета
                    self.slots[i] = {'id': i, 'color': (255, 0, 0)}
                else:
                    self.slots[i] = None

def main():
    inventory = Inventory()
    running = True
    
    while running:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Левый клик
                    inventory.handle_click(mouse_pos)

        screen.fill((200, 200, 200))
        inventory.draw(screen)
        
        # Визуализация курсора над слотом
        hover_slot = None
        for i, rect in enumerate(inventory.slot_rects):
            if rect.collidepoint(mouse_pos):
                hover_slot = i
                break
        
        if hover_slot is not None:
            pygame.draw.rect(screen, (255, 255, 0), inventory.slot_rects[hover_slot], 2)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
