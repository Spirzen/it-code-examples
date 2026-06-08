from collections import deque

def bfs(grid, sr, sc):
    rows, cols = len(grid), len(grid[0])
    q = deque([(sr, sc, 0)])    # очередь: (строка, столбец, расстояние)
    seen = {(sr, sc)}
    while q:
        r, c, dist = q.popleft()
        if grid[r][c] == "G":   # цель — клетка 'G'
            return dist
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#":
                if (nr, nc) not in seen:
                    seen.add((nr, nc))
                    q.append((nr, nc, dist + 1))
    return -1

rows, cols = map(int, inputsplit())
grid = [inputstrip() for _ in range(rows)]
sr, sc = map(int, inputsplit())
print(bfs(grid, sr - 1, sc - 1))
