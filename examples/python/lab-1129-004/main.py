import numpy as np

a = np.array([10, 20, 30, 40, 50])
print("Первый:", a[0], "  Последний:", a[-1])
print("Срез [1:4]:", a[1:4])   # индексы 1,2,3

m = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print("\nЯчейка [1,2] (строка 1, столб 2):", m[1, 2])
print("Строка 0 целиком:", m[0, :])
print("Столбец 1:", m[:, 1])

temperatures = np.array([-5, 0, 12, 25, -2])
mask = temperatures > 0
warm = temperatures[mask]
print("\nМаска >0:", mask)
print("Только тепло:", warm)
