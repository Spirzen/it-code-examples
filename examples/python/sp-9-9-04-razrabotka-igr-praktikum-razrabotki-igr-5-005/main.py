import settings as S

# Смещения (dx, dy) относительно (x, y) фигуры — «нулевой» поворот
SHAPES = {
    "I": [(0, 0), (-1, 0), (1, 0), (2, 0)],
    "O": [(0, 0), (1, 0), (0, 1), (1, 1)],
    "T": [(0, 0), (-1, 0), (1, 0), (0, 1)],
    "S": [(0, 0), (1, 0), (0, 1), (-1, 1)],
    "Z": [(0, 0), (-1, 0), (0, 1), (1, 1)],
    "J": [(0, 0), (-1, 0), (0, 1), (0, 2)],
    "L": [(0, 0), (1, 0), (0, 1), (0, 2)],
}

KIND_TO_ID = {
    "I": 1, "O": 2, "T": 3, "S": 4, "Z": 5, "J": 6, "L": 7,
}


def rotate_cw(cells):
    """Поворот 90° по часовой стрелке."""
    return [(-dy, dx) for dx, dy in cells]


def rotate_ccw(cells):
    """Поворот 90° против часовой стрелки."""
    return [(dy, -dx) for dx, dy in cells]


def color_for_kind(kind):
    return S.COLORS[KIND_TO_ID[kind]]
