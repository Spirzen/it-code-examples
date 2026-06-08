from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Загрузка данных
iris = load_iris()
X, y = iris.data, iris.target

# Разделение и масштабирование
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Обучение модели
clf = GaussianNB()
clf.fit(X_train_scaled, y_train)

# Прогнозирование и вероятности
predictions = clf.predict(X_test_scaled)
probabilities = clf.predict_proba(X_test_scaled)
