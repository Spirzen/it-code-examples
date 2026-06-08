from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

import pandas as pd
import numpy as np

# Загрузка данных о клиентах
data = pd.read_csv('customer_behavior.csv')
features = data[['session_duration', 'pages_viewed', 'purchase_amount']]

# Нормализация признаков
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Кластеризация на 4 группы
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
data['cluster'] = kmeans.fit_predict(scaled_features)

# Анализ характеристик каждого кластера
for cluster_id in range(4):
    cluster_data = data[data['cluster'] == cluster_id]
    print(f"Кластер {cluster_id}: {len(cluster_data)} клиентов")
    print(f"  Средняя длительность сессии: {cluster_data['session_duration'].mean():.1f} мин")
    print(f"  Средний чек: {cluster_data['purchase_amount'].mean():.2f} руб")
