import numpy as np

u = np.array([1, 2, 3])
v = np.array([4, 5, 6])
dot_uv = np.dot(u, v)
print("u·v = 1*4+2*5+3*6 =", dot_uv)

A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])
C = A @ B
print("\nA @ B =\n", C)
print("\nB @ A =\n", B @ A)
