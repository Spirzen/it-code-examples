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
