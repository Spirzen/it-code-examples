
import math

angle = math.pi / 4  # 45°
cos_a, sin_a = math.cos(angle), math.sin(angle)

# Поворот вокруг начала координат
R = [
    [cos_a, -sin_a, 0],
    [sin_a,  cos_a, 0],
    [0, 0, 1],
]
# Сдвиг
T = [
    [1, 0, 10],
    [0, 1, 20],
    [0, 0, 1],
]

def mul3(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

def mul3v(M, p):
    return [sum(M[i][j] * p[j] for j in range(3)) for i in range(3)]

M = mul3(T, R)
p = [1, 0, 1]  # точка (1, 0)
x, y, w = mul3v(M, p)
print(round(x / w, 2), round(y / w, 2))  # новые координаты
