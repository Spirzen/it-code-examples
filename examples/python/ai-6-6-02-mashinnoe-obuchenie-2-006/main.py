from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.datasets import load_wine

# Загрузка данных
wine = load_wine()
X, y = wine.data, wine.target

# Создание конвейера с масштабированием
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier(
        n_neighbors=5,
        weights='distance',
        algorithm='auto',
        leaf_size=30,
        p=2,
        metric='minkowski'
    ))
])

# Обучение модели
pipeline.fit(X, y)

# Получение расстояний до соседей для нового объекта
distances, indices = pipeline.named_steps['knn'].kneighbors(X[:1])
