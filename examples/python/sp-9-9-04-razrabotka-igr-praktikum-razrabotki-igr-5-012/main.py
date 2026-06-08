def draw_next_preview(surface, kind):
    px = S.MARGIN + S.BOARD_W + 36
    py = S.MARGIN + 72
    font = pygame.font.SysFont("consolas", 18)
    surface.blit(font.render("NEXT", True, S.COLOR_TEXT), (px, py - 24))

    cells = T.SHAPES[kind]
    min_dx = min(dx for dx, dy in cells)
    min_dy = min(dy for dx, dy in cells)
    for dx, dy in cells:
        x = px + (dx - min_dx) * (S.CELL_SIZE - 4)
        y = py + (dy - min_dy) * (S.CELL_SIZE - 4)
        rect = pygame.Rect(x, y, S.CELL_SIZE - 6, S.CELL_SIZE - 6)
        pygame.draw.rect(surface, T.color_for_kind(kind), rect, border_radius=2)
