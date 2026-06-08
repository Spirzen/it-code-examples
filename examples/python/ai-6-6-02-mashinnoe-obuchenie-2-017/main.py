from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_breast_cancer

import matplotlib.pyplot as plt

# Загрузка данных
data = load_breast_cancer()
X = data.data
y = data.target

# Масштабирование
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Применение PCA
pca = PCA(n_components=0.95)  # Сохранение 95% дисперсии
X_pca = pca.fit_transform(X_scaled)

# Количество компонент для достижения цели
n_components = pca.n_components_

# Доля дисперсии каждой компоненты
explained_variance_ratio = pca.explained_variance_ratio_

# Визуализация первых двух компонент
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis', alpha=0.6)
plt.xlabel('Первая главная компонента')
plt.ylabel('Вторая главная компонента')
