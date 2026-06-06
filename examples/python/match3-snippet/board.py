from dataclasses import dataclass

@dataclass(frozen=True)
class Cell:
    row: int
    col: int
    gem: int

class Board:
    def __init__(self, rows: int, cols: int, fill: int = 0):
        self.rows = rows
        self.cols = cols
        self._cells = [[fill for _ in range(cols)] for _ in range(rows)]

    def get(self, row: int, col: int) -> int:
        return self._cells[row][col]
