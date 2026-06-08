from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

import numpy as np

# Пример оценки регрессионной модели
y_true = np.array([3.5, 2.8, 4.2, 3.1, 5.0, 4.5, 3.8, 4.1, 2.9, 3.6])
y_pred = np.array([3.4, 2.9, 4.0, 3.2, 4.8, 4.6, 3.7, 4.2, 3.0, 3.5])

# Вычисляем метрики
mse = mean_squared_error(y_true, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_true, y_pred)
r2 = r2_score(y_true, y_pred)

print(f"MSE: {mse:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"MAE: {mae:.4f}")
print(f"R²: {r2:.4f}")
