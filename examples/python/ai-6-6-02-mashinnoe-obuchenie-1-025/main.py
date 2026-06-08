
import numpy as np
import pandas as pd

from sklearn.datasets import make_blobs, make_moons
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, davies_bouldin_score

import matplotlib.pyplot as plt
import seaborn as sns

# Создаем синтетические данные
X_blobs, y_blobs = make_blobs(n_samples=500, centers=4, cluster_std=0.60, random_state=42)
X_moons, y_moons = make_moons(n_samples=300, noise=0.1, random_state=42)

# Нормализуем данные
scaler = StandardScaler()
X_blobs_scaled = scaler.fit_transform(X_blobs)
X_moons_scaled = scaler.fit_transform(X_moons)

# K-Means кластеризация
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
kmeans_labels = kmeans.fit_predict(X_blobs_scaled)

# DBSCAN кластеризация
dbscan = DBSCAN(eps=0.3, min_samples=5)
dbscan_labels = dbscan.fit_predict(X_moons_scaled)

# Иерархическая кластеризация
agglo = AgglomerativeClustering(n_clusters=4)
agglo_labels = agglo.fit_predict(X_blobs_scaled)

# Оценка качества кластеризации
silhouette_kmeans = silhouette_score(X_blobs_scaled, kmeans_labels)
silhouette_agglo = silhouette_score(X_blobs_scaled, agglo_labels)
silhouette_dbscan = silhouette_score(X_moons_scaled, dbscan_labels[dbscan_labels != -1])

print(f"Silhouette Score K-Means: {silhouette_kmeans:.4f}")
print(f"Silhouette Score Agglomerative: {silhouette_agglo:.4f}")
print(f"Silhouette Score DBSCAN: {silhouette_dbscan:.4f}")

# Визуализация результатов
fig, axes = plt.subplots(2, 2, figsize=(14, 12))

# Исходные данные
axes[0, 0].scatter(X_blobs[:, 0], X_blobs[:, 1], c=y_blobs, cmap='viridis', alpha=0.6)
axes[0, 0].set_title('Исходные данные (blobs)')
axes[0, 0].grid(True)

# K-Means результаты
axes[0, 1].scatter(X_blobs[:, 0], X_blobs[:, 1], c=kmeans_labels, cmap='viridis', alpha=0.6)
axes[0, 1].scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
                  c='red', marker='X', s=200, label='Центроиды')
axes[0, 1].set_title('K-Means кластеризация')
axes[0, 1].legend()
axes[0, 1].grid(True)

# DBSCAN результаты
axes[1, 0].scatter(X_moons[:, 0], X_moons[:, 1], c=dbscan_labels, cmap='viridis', alpha=0.6)
axes[1, 0].set_title('DBSCAN кластеризация')
axes[1, 0].grid(True)

# Иерархическая кластеризация
axes[1, 1].scatter(X_blobs[:, 0], X_blobs[:, 1], c=agglo_labels, cmap='viridis', alpha=0.6)
axes[1, 1].set_title('Иерархическая кластеризация')
axes[1, 1].grid(True)

plt.tight_layout()
plt.show()

# Определение оптимального числа кластеров
inertias = []
silhouettes = []
k_range = range(2, 11)

for k in k_range:
    kmeans_temp = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans_temp.fit_predict(X_blobs_scaled)
    inertias.append(kmeans_temp.inertia_)
    silhouettes.append(silhouette_score(X_blobs_scaled, labels))

# График метода локтя
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.plot(k_range, inertias, 'bo-')
ax1.set_xlabel('Количество кластеров')
ax1.set_ylabel('Инерция')
ax1.set_title('Метод локтя')
ax1.grid(True)

ax2.plot(k_range, silhouettes, 'ro-')
ax2.set_xlabel('Количество кластеров')
ax2.set_ylabel('Silhouette Score')
ax2.set_title('Silhouette Score')
ax2.grid(True)

plt.tight_layout()
plt.show()
