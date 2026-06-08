class Match3Game:
    def __init__(self):
        self.grid = [[random.randint(1, 5) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.selected = None
        self.hover = None
        self.ensure_no_matches_on_start()

    def ensure_no_matches_on_start(self):
        changed = True
        while changed:
            changed = False
            for y in range(GRID_SIZE):
                for x in range(GRID_SIZE):
                    if self.has_match_at(x, y):
                        self.grid[y][x] = random.randint(1, 5)
                        changed = True

    def has_match_at(self, x, y):
        if x >= 2 and self.grid[y][x] == self.grid[y][x - 1] == self.grid[y][x - 2]:
            return True
        if x < GRID_SIZE - 2 and self.grid[y][x] == self.grid[y][x + 1] == self.grid[y][x + 2]:
            return True
        if y >= 2 and self.grid[y][x] == self.grid[y - 1][x] == self.grid[y - 2][x]:
            return True
        if y < GRID_SIZE - 2 and self.grid[y][x] == self.grid[y + 1][x] == self.grid[y + 2][x]:
            return True
        return False

    def get_tile_pos(self, pos):
        mx, my = pos
        if not (PLAY_OX <= mx < PLAY_OX + BOARD_INNER and PLAY_OY <= my < PLAY_OY + BOARD_INNER):
            return None, None
        col = (mx - PLAY_OX) // (TILE_SIZE + CELL_GAP)
        row = (my - PLAY_OY) // (TILE_SIZE + CELL_GAP)
        if 0 <= col < GRID_SIZE and 0 <= row < GRID_SIZE:
            return int(col), int(row)
        return None, None
