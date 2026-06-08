import pygame
import settings as S


def _font(size):
    return pygame.font.SysFont("consolas", size)


def draw_score(surface, left, right):
    text = _font(36).render(f"{left}  :  {right}", True, S.COLOR_TEXT)
    surface.blit(text, text.get_rect(center=(S.SCREEN_W // 2, 28)))


def draw_center_message(surface, title, subtitle=""):
    overlay = pygame.Surface((S.SCREEN_W, S.SCREEN_H), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 140))
    surface.blit(overlay, (0, 0))

    t1 = _font(48).render(title, True, S.COLOR_ACCENT)
    surface.blit(t1, t1.get_rect(center=(S.SCREEN_W // 2, S.SCREEN_H // 2 - 20)))

    if subtitle:
        t2 = _font(22).render(subtitle, True, S.COLOR_TEXT)
        surface.blit(t2, t2.get_rect(center=(S.SCREEN_W // 2, S.SCREEN_H // 2 + 30)))


def draw_menu(surface):
    draw_center_message(surface, "PING PONG", "Пробел — начать матч")


def draw_paused(surface):
    draw_center_message(surface, "ПАУЗА", "P — продолжить")


def draw_win(surface, winner_name):
    draw_center_message(surface, f"Победа: {winner_name}", "R — новый матч")
