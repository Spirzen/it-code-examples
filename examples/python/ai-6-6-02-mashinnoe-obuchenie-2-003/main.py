from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

# Генерация синтетических данных
X, y = make_classification(
    n_samples=1000,
    n_features=20,
    n_informative=15,
    n_redundant=5,
    random_state=42
)

# Создание и обучение случайного леса
clf = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    min_samples_split=2,
    max_features='sqrt',
    bootstrap=True,
    oob_score=True,
    n_jobs=-1,
    random_state=42
)
clf.fit(X, y)

# Оценка важности признаков
importances = clf.feature_importances_
