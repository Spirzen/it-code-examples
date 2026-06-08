# Python — полный цикл обработки данных в нейросети

import numpy as np

def sigmoid(x):
    """Функция активации сигмоида"""
    return 1 / (1 + np.exp(-x))

# Исходные данные (например, признаки объекта)
input_data = np.array([0.5, 0.8, -0.3])

# Веса первого скрытого слоя (3 входа → 4 нейрона)
weights_hidden1 = np.array([
    [0.2, 0.4, -0.5, 0.1],
    [0.6, -0.3, 0.7, 0.2],
    [-0.4, 0.5, 0.1, -0.6]
])

# Веса выходного слоя (4 нейрона → 1 выход)
weights_output = np.array([0.3, -0.7, 0.4, 0.8])
bias_output = 0.1

# Обработка во входном слое (просто передача данных)
layer_input = input_data

# Вычисления в первом скрытом слое
hidden1_input = np.dot(layer_input, weights_hidden1)
hidden1_output = sigmoid(hidden1_input)

# Вычисления в выходном слое
output_input = np.dot(hidden1_output, weights_output) + bias_output
final_output = sigmoid(output_input)

print(f"Исходные данные: {input_data}")
print(f"Выход скрытого слоя: {hidden1_output}")
print(f"Результат сети: {final_output}")
