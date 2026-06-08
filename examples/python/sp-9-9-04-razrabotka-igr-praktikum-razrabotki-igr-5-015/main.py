import settings as S

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

ALL_KINDS = list(SHAPES.keys())
LINE_SCORES = {1: 40, 2: 100, 3: 300, 4: 1200}


def rotate_cw(cells):
    return [(-dy, dx) for dx, dy in cells]


def rotate_ccw(cells):
    return [(dy, -dx) for dx, dy in cells]


def color_for_kind(kind):
    return S.COLORS[KIND_TO_ID[kind]]


def color_for_id(color_id):
    return S.COLORS[color_id]


def gravity_interval(level):
    return max(0.05, 0.8 - level * 0.07)
