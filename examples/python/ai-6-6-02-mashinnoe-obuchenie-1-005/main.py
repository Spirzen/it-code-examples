from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

# Загружаем данные
wine = load_wine()
X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.3)

# Создаем и обучаем модель
model = RandomForestClassifier(n_estimators=100, max_depth=10)
model.fit(X_train, y_train)

# Оцениваем модель
accuracy = model.score(X_test, y_test)
print(f"Точность случайного леса: {accuracy:.2f}")
