from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_blobs

import numpy as np

# Генерация данных с естественными кластерами
X, true_labels = make_blobs(
    n_samples=1000,
    centers=5,
    cluster_std=0.6,
    random_state=42
)

# Масштабирование признаков
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Обучение модели K-средних
kmeans = KMeans(
    n_clusters=5,
    init='k-means++',
    n_init=10,
    max_iter=300,
    random_state=42
)
cluster_labels = kmeans.fit_predict(X_scaled)

# Центроиды кластеров в исходном масштабе
centroids = scaler.inverse_transform(kmeans.cluster_centers_)

# Оценка качества кластеризации
from sklearn.metrics import silhouette_score
silhouette = silhouette_score(X_scaled, cluster_labels)
