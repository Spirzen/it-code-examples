from sklearn.metrics import (
    mean_absolute_error, mean_squared_error, r2_score, mean_absolute_percentage_error
)
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor

import numpy as np

# Генерация данных регрессии
X, y = make_regression(
    n_samples=1000,
    n_features=30,
    n_informative=20,
    noise=10.0,
    random_state=42
)

# Разделение данных
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Обучение модели
reg = GradientBoostingRegressor(
    n_estimators=200,
    max_depth=5,
    learning_rate=0.1,
    random_state=42
)
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)

# Вычисление метрик
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
mape = mean_absolute_percentage_error(y_test, y_pred)

print(f"Средняя абсолютная ошибка (MAE): {mae:.4f}")
print(f"Средняя квадратичная ошибка (MSE): {mse:.4f}")
print(f"Корень из MSE (RMSE): {rmse:.4f}")
print(f"Коэффициент детерминации (R²): {r2:.4f}")
print(f"Средняя абсолютная процентная ошибка (MAPE): {mape:.2%}")
