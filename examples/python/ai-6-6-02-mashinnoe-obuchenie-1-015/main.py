from sklearn.model_selection import cross_val_score, KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

# Загружаем данные
iris = load_iris()
X, y = iris.data, iris.target

# Создаем модель
model = RandomForestClassifier(n_estimators=100)

# K-fold кросс-валидация
kfold = KFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=kfold, scoring='accuracy')

print(f"Средняя точность: {scores.mean():.4f} (+/- {scores.std() * 2:.4f})")
print(f"Оценки по фолдам: {scores}")
