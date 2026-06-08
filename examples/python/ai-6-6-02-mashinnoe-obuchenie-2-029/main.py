from sklearn.neighbors import LocalOutlierFactor

import matplotlib.pyplot as plt

# Применение LOF
lof = LocalOutlierFactor(
    n_neighbors=20,
    contamination=0.05,
    novelty=False
)
lof_predictions = lof.fit_predict(X_scaled)
lof_scores = -lof.negative_outlier_factor_

# Визуализация результатов
plt.figure(figsize=(12, 5))

# Исходные данные
plt.subplot(1, 2, 1)
plt.scatter(X[:, 0], X[:, 1], c='blue', alpha=0.6, label='Нормальные')
plt.scatter(X[lof_predictions == -1, 0], X[lof_predictions == -1, 1], 
           c='red', alpha=0.8, label='Аномалии')
plt.title('LOF: обнаруженные аномалии')
plt.legend()

# Распределение оценок аномальности
plt.subplot(1, 2, 2)
plt.hist(lof_scores, bins=50, color='green', alpha=0.7)
plt.axvline(x=np.percentile(lof_scores, 95), color='red', linestyle='--', label='Порог 95%')
plt.title('Распределение оценок аномальности LOF')
plt.xlabel('Оценка аномальности')
plt.ylabel('Частота')
plt.legend()

plt.tight_layout()
