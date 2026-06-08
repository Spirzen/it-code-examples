    def try_rotate(self, board, direction=1):
        if self.kind == "O":
            return True  # квадрат не меняется

        old = self.cells
        new_cells = T.rotate_cw(old) if direction == 1 else T.rotate_ccw(old)

        # Пробуем поворот и небольшие сдвиги (wall kick)
        for kick_dx, kick_dy in [(0, 0), (-1, 0), (1, 0), (0, -1), (-2, 0), (2, 0)]:
            if can_place(board, new_cells, self.x + kick_dx, self.y + kick_dy):
                self.cells = new_cells
                self.x += kick_dx
                self.y += kick_dy
                return True
        return False
