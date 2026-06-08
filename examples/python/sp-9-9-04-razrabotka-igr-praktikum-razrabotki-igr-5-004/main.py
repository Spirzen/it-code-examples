def board_origin():
    return S.MARGIN, S.MARGIN


def draw_board(surface):
    ox, oy = board_origin()
    field = pygame.Rect(ox, oy, S.BOARD_W, S.BOARD_H)
    pygame.draw.rect(surface, S.COLOR_GRID, field)

    # Вертикальные линии
    for col in range(S.COLS + 1):
        x = ox + col * S.CELL_SIZE
        pygame.draw.line(
            surface, S.COLOR_GRID_LINE,
            (x, oy), (x, oy + S.BOARD_H),
        )

    # Горизонтальные линии
    for row in range(S.ROWS + 1):
        y = oy + row * S.CELL_SIZE
        pygame.draw.line(
            surface, S.COLOR_GRID_LINE,
            (ox, y), (ox + S.BOARD_W, y),
        )

    pygame.draw.rect(surface, S.COLOR_GRID_LINE, field, width=2)


def draw_sidebar(surface):
    ox = S.MARGIN + S.BOARD_W + 12
    oy = S.MARGIN
    panel = pygame.Rect(ox, oy, S.SIDEBAR_W - 12, S.BOARD_H)
    pygame.draw.rect(surface, S.COLOR_SIDEBAR, panel, border_radius=6)
    pygame.draw.rect(surface, S.COLOR_GRID_LINE, panel, width=1, border_radius=6)
