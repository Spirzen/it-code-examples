from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import pandas as pd

# Загрузка размеченных данных
data = pd.read_csv('customer_data.csv')
X = data[['age', 'income', 'purchase_frequency']]
y = data['churn_risk']  # Целевая переменная: 0 или 1

# Разделение на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Обучение модели случайного леса
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Оценка точности
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Точность модели: {accuracy:.2f}")
