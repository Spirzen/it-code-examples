from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_blobs

import numpy as np

# Генерация данных с аномалиями
np.random.seed(42)
X_normal, _ = make_blobs(n_samples=1000, centers=3, cluster_std=1.0, random_state=42)
X_anomalies = np.random.uniform(low=-10, high=10, size=(50, 2))
X = np.vstack([X_normal, X_anomalies])

# Масштабирование данных
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Создание и обучение изолирующего леса
iso_forest = IsolationForest(
    n_estimators=100,
    max_samples='auto',
    contamination=0.05,
    random_state=42,
    n_jobs=-1
)
iso_forest.fit(X_scaled)

# Предсказание аномалий (-1 для аномалий, 1 для нормальных)
predictions = iso_forest.predict(X_scaled)
anomaly_scores = iso_forest.score_samples(X_scaled)

# Идентификация аномальных объектов
anomaly_indices = np.where(predictions == -1)[0]
print(f"Обнаружено аномалий: {len(anomaly_indices)}")
print(f"Индексы аномалий: {anomaly_indices[:10]}")
print(f"Оценки аномальности для первых 10 объектов: {anomaly_scores[:10]}")
