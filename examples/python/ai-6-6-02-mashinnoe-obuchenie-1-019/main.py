
import numpy as np

# Создание массивов
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Операции с массивами
sum_arr = arr1 + 10
product = arr1 * 2
dot_product = np.dot(arr1, arr1)

# Статистические функции
mean_val = np.mean(arr1)
std_val = np.std(arr1)
max_val = np.max(arr1)

# Создание специальных массивов
zeros = np.zeros((3, 3))
ones = np.ones((2, 4))
identity = np.eye(4)
random_arr = np.random.rand(3, 3)

print("Исходный массив:", arr1)
print("Сумма с 10:", sum_arr)
print("Среднее значение:", mean_val)
print("Матрица нулей:\n", zeros)
