def bresenham(x0, y0, x1, y1):
    """Генератор пикселей отрезка (целочисленный Брезенхем)."""
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    x, y = x0, y0
    while True:
        yield x, y
        if x == x1 and y == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy

# Мини-"растр" 12×8 для отрезка (1,1)— (10,6)
w, h = 12, 8
grid = [['.' for _ in range(w)] for _ in range(h)]
for x, y in bresenham(1, 1, 10, 6):
    grid[h - 1 - y][x] = '#'
print('\n'.join(''.join(row) for row in grid))
