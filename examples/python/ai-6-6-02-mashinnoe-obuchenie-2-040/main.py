
import numpy as np
import pandas as pd

from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_absolute_error, mean_squared_error

import matplotlib.pyplot as plt

# Генерация синтетического временного ряда с сезонностью
np.random.seed(42)
date_range = pd.date_range(start='2020-01-01', periods=400, freq='D')
trend = np.linspace(0, 50, 400)
seasonality = 20 * np.sin(2 * np.pi * np.arange(400) / 365)
noise = np.random.normal(0, 5, 400)
values = trend + seasonality + noise

series = pd.Series(values, index=date_range)

# Разделение на обучающую и тестовую выборки (хронологически)
train_size = int(len(series) * 0.8)
train_series = series[:train_size]
test_series = series[train_size:]

# Подбор и обучение модели SARIMA
model = SARIMAX(
    train_series,
    order=(2, 1, 2),           # ARIMA компоненты
    seasonal_order=(1, 1, 1, 365),  # Сезонные компоненты с годовым периодом
    enforce_stationarity=False,
    enforce_invertibility=False
)

results = model.fit(disp=False)

# Прогнозирование на тестовом периоде
forecast = results.get_forecast(steps=len(test_series))
forecast_mean = forecast.predicted_mean
forecast_ci = forecast.conf_int()

# Оценка качества
mae = mean_absolute_error(test_series, forecast_mean)
rmse = np.sqrt(mean_squared_error(test_series, forecast_mean))

print(f"MAE: {mae:.2f}")
print(f"RMSE: {rmse:.2f}")

# Визуализация результатов
plt.figure(figsize=(14, 6))
plt.plot(train_series.index, train_series, label='Обучающие данные')
plt.plot(test_series.index, test_series, label='Фактические значения', alpha=0.6)
plt.plot(test_series.index, forecast_mean, label='Прогноз', color='red')
plt.fill_between(
    test_series.index,
    forecast_ci.iloc[:, 0],
    forecast_ci.iloc[:, 1],
    color='pink',
    alpha=0.3,
    label='95% доверительный интервал'
)
plt.title('Прогноз временного ряда с помощью SARIMA')
plt.xlabel('Дата')
plt.ylabel('Значение')
plt.legend()
plt.grid(True, alpha=0.3)
