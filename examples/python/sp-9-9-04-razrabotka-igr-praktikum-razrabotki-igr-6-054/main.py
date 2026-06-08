import pygame

from core.config import SCREEN_HEIGHT, SCREEN_WIDTH, UI_TEXT


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

    def draw_pause(self, screen) -> None:
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((12, 14, 26, 180))
        screen.blit(overlay, (0, 0))
        font = pygame.font.SysFont("Segoe UI", 36, bold=True)
        text = font.render("Пауза — Esc", True, UI_TEXT)
        screen.blit(text, text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))

    def draw_game_over(self, screen) -> None:
        font = pygame.font.SysFont("Segoe UI", 48, bold=True)
        text = font.render("Game Over", True, (220, 80, 80))
        screen.blit(text, text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))
        hint = pygame.font.SysFont("Segoe UI", 22).render("Esc — в меню", True, UI_TEXT)
        screen.blit(hint, hint.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 56)))
