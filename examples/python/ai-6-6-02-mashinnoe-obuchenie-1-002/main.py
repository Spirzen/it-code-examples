from sklearn.linear_model import LinearRegression

import numpy as np

# Создаем данные
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 4, 5])

# Создаем и обучаем модель
model = LinearRegression()
model.fit(X, y)

# Предсказываем
predictions = model.predict([[6]])
print(f"Предсказание для значения 6: {predictions[0]}")
