def new_board():
    return [[0 for _ in range(S.COLS)] for _ in range(S.ROWS)]


def draw_locked_blocks(surface, board):
    ox, oy = board_origin()
    for row in range(S.ROWS):
        for col in range(S.COLS):
            cell = board[row][col]
            if cell:
                px = ox + col * S.CELL_SIZE
                py = oy + row * S.CELL_SIZE
                rect = pygame.Rect(px + 1, py + 1, S.CELL_SIZE - 2, S.CELL_SIZE - 2)
                pygame.draw.rect(surface, S.COLORS[cell], rect, border_radius=3)
