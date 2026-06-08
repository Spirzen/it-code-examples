import pygame
import settings as S


def draw_court(surface):
    field = pygame.Rect(S.MARGIN, S.MARGIN, S.FIELD_W, S.FIELD_H)
    pygame.draw.rect(surface, S.COLOR_FIELD, field, border_radius=4)
    pygame.draw.rect(surface, S.COLOR_LINE, field, width=2, border_radius=4)

    center_x = S.MARGIN + S.FIELD_W // 2
    dash_h = 16
    gap = 12
    y = S.MARGIN
    while y < S.MARGIN + S.FIELD_H:
        pygame.draw.line(
            surface,
            S.COLOR_LINE,
            (center_x, y),
            (center_x, min(y + dash_h, S.MARGIN + S.FIELD_H)),
            2,
        )
        y += dash_h + gap


def field_rect():
    return pygame.Rect(S.MARGIN, S.MARGIN, S.FIELD_W, S.FIELD_H)
