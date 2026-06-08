from tensorflow.keras.layers import GRU, TimeDistributed

import pandas as pd

# Генерация многомерного временного ряда
np.random.seed(42)
n_samples = 1000
n_timesteps = 50
n_features = 5

# Создание временных рядов с сезонными компонентами
time_index = np.arange(n_timesteps)
series_data = []
targets = []

for _ in range(n_samples):
    sample = np.zeros((n_timesteps, n_features))
    for feature in range(n_features):
        # Сезонная компонента разной частоты для каждого признака
        freq = 2 * np.pi * (feature + 1) / n_timesteps
        seasonal = 10 * np.sin(freq * time_index)
        noise = np.random.normal(0, 2, n_timesteps)
        sample[:, feature] = seasonal + noise
    
    series_data.append(sample)
    # Целевая переменная — значение первого признака на следующем шаге
    targets.append(sample[-1, 0] + np.random.normal(0, 1))

X = np.array(series_data)
y = np.array(targets)

# Разделение данных
split_idx = int(n_samples * 0.8)
X_train, X_test = X[:split_idx], X[split_idx:]
y_train, y_test = y[:split_idx], y[split_idx:]

# Модель с GRU для регрессии
regression_model = Sequential([
    GRU(128, input_shape=(n_timesteps, n_features), return_sequences=True),
    Dropout(0.2),
    GRU(64),
    Dropout(0.2),
    Dense(32, activation='relu'),
    Dense(1)
])

regression_model.compile(
    optimizer='adam',
    loss='mse',
    metrics=['mae']
)

regression_model.fit(
    X_train, y_train,
    epochs=30,
    batch_size=64,
    validation_split=0.1,
    verbose=1
)

# Оценка
mae = regression_model.evaluate(X_test, y_test, verbose=0)[1]
print(f"Средняя абсолютная ошибка прогноза: {mae:.2f}")
