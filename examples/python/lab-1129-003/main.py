import numpy as np

# Целые: 0, 2, 4, 6, 8 (10 не входит)
evens = np.arange(0, 10, 2)
print("arange:", evens)

# Ровно 5 точек от 0 до 1 включительно
grid = np.linspace(0, 1, num=5)
print("linspace:", grid)

# Пара (x, y) для sin — типичный старт Matplotlib
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
print("x: от", x[0], "до", x[-1])
print("y[0]≈0, y[25]≈1, y[-1]≈0:", round(y[0], 3), round(y[25], 3), round(y[-1], 3))
