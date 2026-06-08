from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

# Загружаем данные
cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.3)

# Создаем и обучаем модель
model = DecisionTreeClassifier(max_depth=5)
model.fit(X_train, y_train)

# Оцениваем модель
accuracy = model.score(X_test, y_test)
print(f"Точность дерева решений: {accuracy:.2f}")
