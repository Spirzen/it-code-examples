import numpy as np
import time

n = 1_000_000
py_list = list(range(n))
np_arr = np.arange(n)

# Сложение
t0 = time.perf_counter()
py_sum = [a + 1 for a in py_list]
t_list = time.perf_counter() - t0

t0 = time.perf_counter()
np_sum = np_arr + 1
t_numpy = time.perf_counter() - t0

print(f"Список: {t_list:.3f} с")
print(f"NumPy:  {t_numpy:.3f} с")
print("Первые 5 (NumPy):", np_sum[:5])
