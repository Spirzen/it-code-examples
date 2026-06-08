from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)

# Создание модели
model = KNeighborsClassifier(n_neighbors=5)

# Обучение модели
model.fit(X_train, y_train)

# Предсказание
predictions = model.predict(X_test)

# Оценка качества
score = accuracy_score(y_test, predictions)
print(f"Точность модели: {score:.2%}")
