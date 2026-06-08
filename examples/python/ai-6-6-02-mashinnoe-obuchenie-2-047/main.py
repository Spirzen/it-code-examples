from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification

import numpy as np

# Генерация синтетических данных
X, y = make_classification(
    n_samples=10000,
    n_features=50,
    n_informative=30,
    n_redundant=20,
    random_state=42
)

# Разделение на пакеты для имитации потоковых данных
batch_size = 100
n_batches = len(X) // batch_size

# Инициализация онлайн-классификатора
scaler = StandardScaler()
classifier = SGDClassifier(
    loss='log_loss',  # логистическая регрессия
    penalty='l2',
    alpha=0.0001,
    max_iter=1,
    tol=None,
    shuffle=False,
    random_state=42,
    warm_start=True  # сохранение весов между вызовами fit
)

# Онлайн-обучение по пакетам
accuracies = []
for batch_idx in range(n_batches):
    start = batch_idx * batch_size
    end = start + batch_size
    X_batch = X[start:end]
    y_batch = y[start:end]
    
    # Масштабирование на основе накопленной статистики
    if batch_idx == 0:
        scaler.partial_fit(X_batch)
    else:
        scaler.partial_fit(X_batch)
    
    X_batch_scaled = scaler.transform(X_batch)
    
    # Обучение на текущем пакете
    classifier.partial_fit(X_batch_scaled, y_batch, classes=np.unique(y))
    
    # Оценка качества на всех обработанных данных
    X_seen = X[:end]
    y_seen = y[:end]
    X_seen_scaled = scaler.transform(X_seen)
    accuracy = classifier.score(X_seen_scaled, y_seen)
    accuracies.append(accuracy)
    
    if batch_idx % 10 == 0:
        print(f"Пакет {batch_idx}/{n_batches}, точность: {accuracy:.4f}")

# Визуализация динамики качества

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(range(len(accuracies)), accuracies, linewidth=2)
plt.xlabel('Номер пакета')
plt.ylabel('Точность на накопленных данных')
plt.title('Динамика качества онлайн-обучения')
plt.grid(True, alpha=0.3)
plt.savefig('online_learning_progress.png')
plt.close()
