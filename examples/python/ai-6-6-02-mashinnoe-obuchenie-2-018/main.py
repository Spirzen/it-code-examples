from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_digits

import matplotlib.pyplot as plt

# Загрузка данных цифр
digits = load_digits()
X = digits.data
y = digits.target

# Масштабирование
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Применение t-SNE
tsne = TSNE(
    n_components=2,
    perplexity=30,
    learning_rate='auto',
    init='pca',
    random_state=42,
    n_iter=1000
)
X_tsne = tsne.fit_transform(X_scaled)

# Визуализация
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y, cmap='tab10', alpha=0.6)
plt.title('Визуализация цифр через t-SNE')
