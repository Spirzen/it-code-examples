from sklearn.svm import SVC
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Загружаем данные
digits = load_digits()
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.3)

# Нормализуем данные
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Создаем и обучаем модель
model = SVC(kernel='rbf', C=10)
model.fit(X_train_scaled, y_train)

# Оцениваем модель
accuracy = model.score(X_test_scaled, y_test)
print(f"Точность SVM: {accuracy:.2f}")
