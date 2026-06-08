from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.datasets import make_classification

# Генерация данных
X, y = make_classification(
    n_samples=1000,
    n_features=20,
    n_informative=15,
    n_redundant=5,
    random_state=42
)

# Создание конвейера с масштабированием и классификатором
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('svm', SVC(
        kernel='rbf',
        C=1.0,
        gamma='scale',
        decision_function_shape='ovr',
        max_iter=-1,
        random_state=42
    ))
])

# Обучение модели
pipeline.fit(X, y)

# Получение опорных векторов
support_vectors = pipeline.named_steps['svm'].support_vectors_
