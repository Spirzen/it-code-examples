# Сетка
COLS = 10
ROWS = 20
CELL_SIZE = 30

# Размеры окна
MARGIN = 24
BOARD_W = COLS * CELL_SIZE
BOARD_H = ROWS * CELL_SIZE
SIDEBAR_W = 160
SCREEN_W = MARGIN * 2 + BOARD_W + SIDEBAR_W
SCREEN_H = MARGIN * 2 + BOARD_H

FPS = 60

# Игровые правила
LINES_PER_LEVEL = 10
SOFT_DROP_BONUS = 1      # очков за клетку при удержании ↓
HARD_DROP_BONUS = 2      # очков за клетку при hard drop
SPAWN_COL = 4
SPAWN_ROW = 0
LOCK_DELAY = 0.5         # секунд до фиксации (этап 20)
SOFT_DROP_INTERVAL = 0.05

# Цвета (R, G, B)
COLOR_BG = (12, 14, 22)
COLOR_GRID = (28, 32, 48)
COLOR_GRID_LINE = (40, 46, 66)
COLOR_TEXT = (220, 225, 235)
COLOR_GHOST = (100, 110, 130)
COLOR_SIDEBAR = (18, 22, 34)

# Цвета тетромино (индекс 1…7)
COLORS = {
    1: (0, 240, 240),    # I — cyan
    2: (240, 240, 0),    # O — yellow
    3: (160, 0, 240),    # T — purple
    4: (0, 240, 0),      # S — green
    5: (240, 0, 0),      # Z — red
    6: (0, 0, 240),      # J — blue
    7: (240, 160, 0),    # L — orange
}
