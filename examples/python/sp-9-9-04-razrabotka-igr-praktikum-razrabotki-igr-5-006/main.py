class Piece:
    def __init__(self, kind, x, y):
        self.kind = kind
        self.x = x
        self.y = y
        self.cells = list(T.SHAPES[kind])
        self.color_id = T.KIND_TO_ID[kind]

    def world_cells(self):
        """Абсолютные координаты клеток на сетке."""
        return [(self.x + dx, self.y + dy) for dx, dy in self.cells]

    def draw(self, surface):
        draw_cells(surface, self.cells, self.x, self.y, T.color_for_kind(self.kind))
