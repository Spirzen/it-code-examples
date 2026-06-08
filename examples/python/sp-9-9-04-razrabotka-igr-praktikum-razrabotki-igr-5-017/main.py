import random
import settings as S
from game import tetrominoes as T
from game.board import can_place


class Piece:
    def __init__(self, kind, x=None, y=None):
        self.kind = kind
        self.x = S.SPAWN_COL if x is None else x
        self.y = S.SPAWN_ROW if y is None else y
        self.cells = list(T.SHAPES[kind])
        self.color_id = T.KIND_TO_ID[kind]

    def world_cells(self):
        return [(self.x + dx, self.y + dy) for dx, dy in self.cells]

    def draw(self, surface):
        from game.board import draw_cell
        for dx, dy in self.cells:
            draw_cell(surface, self.x + dx, self.y + dy, T.color_for_kind(self.kind))

    def try_move(self, board, dx, dy):
        if can_place(board, self.cells, self.x + dx, self.y + dy):
            self.x += dx
            self.y += dy
            return True
        return False

    def try_rotate(self, board, direction=1):
        if self.kind == "O":
            return True
        new_cells = T.rotate_cw(self.cells) if direction == 1 else T.rotate_ccw(self.cells)
        for kick_dx, kick_dy in [(0, 0), (-1, 0), (1, 0), (0, -1), (-2, 0), (2, 0)]:
            if can_place(board, new_cells, self.x + kick_dx, self.y + kick_dy):
                self.cells = new_cells
                self.x += kick_dx
                self.y += kick_dy
                return True
        return False

    def hard_drop(self, board):
        dropped = 0
        while self.try_move(board, 0, 1):
            dropped += 1
        return dropped

    def ghost_row(self, board):
        gy = self.y
        while can_place(board, self.cells, self.x, gy + 1):
            gy += 1
        return gy


def random_kind():
    return random.choice(T.ALL_KINDS)


def spawn_piece(kind):
    return Piece(kind)
