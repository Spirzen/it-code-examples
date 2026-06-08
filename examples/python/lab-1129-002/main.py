import numpy as np

# Одномерный массив — вектор
a = np.array([10, 20, 30])
print("1D:", a)
print("shape:", a.shape, "  ndim:", a.ndim)

# Двумерный — матрица 2 строки × 3 столбца
b = np.array([[1, 2, 3],
              [4, 5, 6]])
print("\n2D:\n", b)
print("shape:", b.shape, "  dtype:", b.dtype)

# Заготовки
zeros = np.zeros((2, 3))
ones = np.ones((3, 2))
identity = np.eye(3)
print("\nzeros (2×3):\n", zeros)
print("\neye (3×3):\n", identity)
