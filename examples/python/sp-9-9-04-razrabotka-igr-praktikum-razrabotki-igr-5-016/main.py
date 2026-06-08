import pygame
import settings as S
from game.tetrominoes import color_for_id


def board_origin():
    return S.MARGIN, S.MARGIN


def new_board():
    return [[0 for _ in range(S.COLS)] for _ in range(S.ROWS)]


def can_place(board, cells, ax, ay):
    for dx, dy in cells:
        col, row = ax + dx, ay + dy
        if col < 0 or col >= S.COLS or row >= S.ROWS:
            return False
        if row >= 0 and board[row][col]:
            return False
    return True


def lock_piece(board, piece):
    for col, row in piece.world_cells():
        if 0 <= row < S.ROWS and 0 <= col < S.COLS:
            board[row][col] = piece.color_id


def clear_lines(board):
    cleared = 0
    row = S.ROWS - 1
    while row >= 0:
        if all(board[row]):
            del board[row]
            board.insert(0, [0] * S.COLS)
            cleared += 1
        else:
            row -= 1
    return cleared


def draw_cell(surface, col, row, color, inset=1):
    ox, oy = board_origin()
    px = ox + col * S.CELL_SIZE
    py = oy + row * S.CELL_SIZE
    rect = pygame.Rect(
        px + inset, py + inset,
        S.CELL_SIZE - 2 * inset, S.CELL_SIZE - 2 * inset,
    )
    pygame.draw.rect(surface, color, rect, border_radius=3)
    highlight = tuple(min(255, c + 35) for c in color)
    pygame.draw.line(surface, highlight, rect.topleft, (rect.right - 1, rect.top), 1)


def draw_board(surface):
    ox, oy = board_origin()
    field = pygame.Rect(ox, oy, S.BOARD_W, S.BOARD_H)
    pygame.draw.rect(surface, S.COLOR_GRID, field)
    for col in range(S.COLS + 1):
        x = ox + col * S.CELL_SIZE
        pygame.draw.line(surface, S.COLOR_GRID_LINE, (x, oy), (x, oy + S.BOARD_H))
    for row in range(S.ROWS + 1):
        y = oy + row * S.CELL_SIZE
        pygame.draw.line(surface, S.COLOR_GRID_LINE, (ox, y), (ox + S.BOARD_W, y))
    pygame.draw.rect(surface, S.COLOR_GRID_LINE, field, width=2)


def draw_locked_blocks(surface, board):
    for row in range(S.ROWS):
        for col in range(S.COLS):
            if board[row][col]:
                draw_cell(surface, col, row, color_for_id(board[row][col]))


def draw_ghost(surface, piece, board):
    gy = piece.ghost_row(board)
    for dx, dy in piece.cells:
        draw_cell(surface, piece.x + dx, gy + dy, S.COLOR_GHOST, inset=3)
