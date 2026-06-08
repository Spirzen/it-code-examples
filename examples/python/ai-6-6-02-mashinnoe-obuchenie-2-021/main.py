
import numpy as np

from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Генерация данных
X, y = make_regression(n_samples=10000, n_features=50, noise=0.1, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Масштабирование
scaler_X = StandardScaler()
scaler_y = StandardScaler()
X_train_scaled = scaler_X.fit_transform(X_train)
y_train_scaled = scaler_y.fit_transform(y_train.reshape(-1, 1)).ravel()

# Инициализация параметров
n_features = X_train_scaled.shape[1]
weights = np.zeros(n_features)
bias = 0.0
learning_rate = 0.01
batch_size = 64
n_epochs = 50

# Обучение
for epoch in range(n_epochs):
    indices = np.random.permutation(len(X_train_scaled))
    for i in range(0, len(X_train_scaled), batch_size):
        batch_indices = indices[i:i + batch_size]
        X_batch = X_train_scaled[batch_indices]
        y_batch = y_train_scaled[batch_indices]
        
        # Прогноз и ошибка
        predictions = X_batch @ weights + bias
        errors = predictions - y_batch
        
        # Градиенты
        grad_weights = (X_batch.T @ errors) / len(batch_indices)
        grad_bias = errors.mean()
        
        # Обновление параметров
        weights -= learning_rate * grad_weights
        bias -= learning_rate * grad_bias
