from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

import numpy as np

# Генерация несбалансированных данных
X, y = make_classification(
    n_samples=2000,
    n_features=40,
    n_informative=30,
    n_redundant=10,
    weights=[0.9, 0.1],
    random_state=42
)

# Создание стратифицированных блоков
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# Модель для оценки
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Выполнение кросс-валидации
scores = cross_val_score(
    clf, X, y, 
    cv=skf, 
    scoring='f1',  # F1-мера для несбалансированных данных
    n_jobs=-1
)

print(f"F1-мера по блокам: {scores}")
print(f"Средняя F1-мера: {scores.mean():.4f} ± {scores.std():.4f}")

# Анализ распределения классов в блоках
print("\nРаспределение классов в блоках:")
for fold, (train_idx, test_idx) in enumerate(skf.split(X, y), 1):
    train_dist = np.bincount(y[train_idx])
    test_dist = np.bincount(y[test_idx])
    print(f"Блок {fold}: обучение {train_dist}, тест {test_dist}")
