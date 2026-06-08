    def find_matches(self):
        matches = []
        for y in range(GRID_SIZE):
            x = 0
            while x < GRID_SIZE - 2:
                color = self.grid[y][x]
                if color == 0:
                    x += 1
                    continue
                end = x
                while end + 1 < GRID_SIZE and self.grid[y][end + 1] == color:
                    end += 1
                if end - x >= 2:
                    matches.append([(y, xi) for xi in range(x, end + 1)])
                    x = end
                x += 1
        for x in range(GRID_SIZE):
            y = 0
            while y < GRID_SIZE - 2:
                color = self.grid[y][x]
                if color == 0:
                    y += 1
                    continue
                end = y
                while end + 1 < GRID_SIZE and self.grid[y][x] == self.grid[end + 1][x]:
                    end += 1
                if end - y >= 2:
                    matches.append([(yi, x) for yi in range(y, end + 1)])
                    y = end
                y += 1
        return matches
