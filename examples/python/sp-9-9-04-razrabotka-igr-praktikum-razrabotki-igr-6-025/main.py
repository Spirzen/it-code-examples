import pygame
from core.config import GameState, SCREEN_HEIGHT, SCREEN_WIDTH, UI_TEXT


class MenuUI:
    def draw(self, screen, selected: int = 0) -> None:
        font = pygame.font.SysFont("Segoe UI", 48, bold=True)
        title = font.render("Pythonablo", True, (255, 204, 96))
        screen.blit(title, title.get_rect(center=(SCREEN_WIDTH // 2, 160)))
        options = ["Новая игра", "Выход"]
        for i, label in enumerate(options):
            f = pygame.font.SysFont("Segoe UI", 28)
            color = (255, 220, 120) if i == selected else UI_TEXT
            t = f.render(label, True, color)
            screen.blit(t, t.get_rect(center=(SCREEN_WIDTH // 2, 320 + i * 48)))
