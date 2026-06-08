BOARD_OX = FRAME
BOARD_OY = HEADER_H + FRAME
GRID_INSET = BOARD_PAD + FRAME // 2 - 3
PLAY_OX = BOARD_OX + GRID_INSET
PLAY_OY = BOARD_OY + GRID_INSET
LOCAL_PLAY_X = GRID_INSET
LOCAL_PLAY_Y = GRID_INSET


def grid_to_pixel(col, row):
    return (
        PLAY_OX + col * (TILE_SIZE + CELL_GAP),
        PLAY_OY + row * (TILE_SIZE + CELL_GAP),
    )


def tile_rect_local(col, row):
    return pygame.Rect(
        LOCAL_PLAY_X + col * (TILE_SIZE + CELL_GAP),
        LOCAL_PLAY_Y + row * (TILE_SIZE + CELL_GAP),
        TILE_SIZE,
        TILE_SIZE,
    )
