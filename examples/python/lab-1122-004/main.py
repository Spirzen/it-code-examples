def dfs(grid, r, c, visited):
    rows, cols = len(grid), len(grid[0])
    if r < 0 or c < 0 or r >= rows or c >= cols:   # вышли за поле
        return
    if grid[r][c] == "#" or (r, c) in visited:     # стена или уже были
        return
    visited.add((r, c))
    dfs(grid, r + 1, c, visited)   # вниз, вверх, вправо, влево
    dfs(grid, r - 1, c, visited)
    dfs(grid, r, c + 1, visited)
    dfs(grid, r, c - 1, visited)

rows, cols = map(int, inputsplit())
grid = [inputstrip() for _ in range(rows)]
visited = set()
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == ".":
            dfs(grid, r, c, visited)
print(len(visited))
