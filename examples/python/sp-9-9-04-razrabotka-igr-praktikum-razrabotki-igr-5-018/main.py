import pygame
import settings as S
from game.tetrominoes import SHAPES, color_for_kind


def draw_sidebar(surface):
    ox = S.MARGIN + S.BOARD_W + 12
    oy = S.MARGIN
    panel = pygame.Rect(ox, oy, S.SIDEBAR_W - 12, S.BOARD_H)
    pygame.draw.rect(surface, S.COLOR_SIDEBAR, panel, border_radius=6)
    pygame.draw.rect(surface, S.COLOR_GRID_LINE, panel, width=1, border_radius=6)


def draw_next_preview(surface, kind):
    px = S.MARGIN + S.BOARD_W + 36
    py = S.MARGIN + 72
    font = pygame.font.SysFont("consolas", 18)
    surface.blit(font.render("NEXT", True, S.COLOR_TEXT), (px, py - 24))
    cells = SHAPES[kind]
    min_dx = min(dx for dx, dy in cells)
    min_dy = min(dy for dx, dy in cells)
    size = S.CELL_SIZE - 6
    for dx, dy in cells:
        rect = pygame.Rect(
            px + (dx - min_dx) * (S.CELL_SIZE - 4),
            py + (dy - min_dy) * (S.CELL_SIZE - 4),
            size, size,
        )
        pygame.draw.rect(surface, color_for_kind(kind), rect, border_radius=2)


def draw_hud(surface, score, lines, level):
    px = S.MARGIN + S.BOARD_W + 24
    y = S.MARGIN + 180
    font = pygame.font.SysFont("consolas", 18)
    for label, value in [("SCORE", score), ("LINES", lines), ("LEVEL", level)]:
        surface.blit(font.render(f"{label}:", True, S.COLOR_TEXT), (px, y))
        surface.blit(font.render(str(value), True, S.COLOR_TEXT), (px, y + 22))
        y += 56


def draw_overlay(surface, title, hint):
    overlay = pygame.Surface((S.SCREEN_W, S.SCREEN_H), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160))
    surface.blit(overlay, (0, 0))
    font_big = pygame.font.SysFont("consolas", 36, bold=True)
    font_small = pygame.font.SysFont("consolas", 20)
    t = font_big.render(title, True, S.COLOR_TEXT)
    h = font_small.render(hint, True, S.COLOR_TEXT)
    surface.blit(t, t.get_rect(center=(S.SCREEN_W // 2, S.SCREEN_H // 2 - 20)))
    surface.blit(h, h.get_rect(center=(S.SCREEN_W // 2, S.SCREEN_H // 2 + 24)))
