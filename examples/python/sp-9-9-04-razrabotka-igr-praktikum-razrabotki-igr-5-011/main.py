def draw_next(surface, kind):
    ox = S.MARGIN + S.BOARD_W + 28
    oy = S.MARGIN + 60
    font = pygame.font.SysFont("consolas", 18)
    title = font.render("NEXT", True, S.COLOR_TEXT)
    surface.blit(title, (ox, oy - 28))

    preview = Piece(kind, 0, 0)
    # Центрируем мини-превью в панели
    cells = preview.cells
    min_dx = min(dx for dx, dy in cells)
    max_dx = max(dx for dx, dy in cells)
    min_dy = min(dy for dx, dy in cells)
    pw = (max_dx - min_dx + 1) * S.CELL_SIZE
    start_col = 1 - min_dx
    start_row = 1 - min_dy
    draw_cells(surface, cells, start_col, start_row, T.color_for_kind(kind))
    # Смещение превью в панель — добавьте смещение origin в draw_cells или рисуйте в локальных координатах
