
import numpy as np
import pandas as pd
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler

import matplotlib.pyplot as plt

# Создаем синтетические данные временного ряда
def create_time_series_data(n_samples=1000):
    time = np.arange(n_samples)
    trend = time * 0.001
    seasonality = np.sin(time * 0.05) * 10
    noise = np.random.randn(n_samples) * 2
    data = trend + seasonality + noise
    return data

# Подготовка данных для обучения
def create_sequences(data, seq_length):
    X, y = [], []
    for i in range(len(data) - seq_length):
        X.append(data[i:i + seq_length])
        y.append(data[i + seq_length])
    return np.array(X), np.array(y)

# Генерируем данные
data = create_time_series_data(2000)

# Нормализуем данные
scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data.reshape(-1, 1)).flatten()

# Создаем последовательности
seq_length = 50
X, y = create_sequences(data_scaled, seq_length)

# Разделяем на обучающий и тестовый наборы
train_size = int(0.8 * len(X))
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# Изменяем форму для LSTM [samples, time steps, features]
X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))

# Создаем модель
model = Sequential([
    LSTM(100, activation='relu', return_sequences=True, input_shape=(seq_length, 1)),
    Dropout(0.2),
    LSTM(50, activation='relu'),
    Dropout(0.2),
    Dense(25, activation='relu'),
    Dense(1)
])

# Компилируем модель
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Обучаем модель
history = model.fit(
    X_train, y_train,
    epochs=50,
    batch_size=32,
    validation_split=0.1,
    verbose=1
)

# Предсказываем
predictions = model.predict(X_test)

# Обратное преобразование к исходному масштабу
predictions_original = scaler.inverse_transform(predictions)
y_test_original = scaler.inverse_transform(y_test.reshape(-1, 1))

# Вычисляем метрики
mse = np.mean((predictions_original - y_test_original) ** 2)
mae = np.mean(np.abs(predictions_original - y_test_original))
print(f"MSE: {mse:.4f}")
print(f"MAE: {mae:.4f}")

# Визуализация результатов
plt.figure(figsize=(14, 6))
plt.plot(y_test_original, label='Фактические значения', alpha=0.7)
plt.plot(predictions_original, label='Предсказания', alpha=0.7)
plt.title('Прогнозирование временных рядов с помощью LSTM')
plt.xlabel('Время')
plt.ylabel('Значение')
plt.legend()
plt.grid(True)
plt.show()
