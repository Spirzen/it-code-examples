from sklearn.ensemble import StackingClassifier
from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# Генерация данных
X, y = make_classification(
    n_samples=5000,
    n_features=30,
    n_informative=20,
    n_redundant=10,
    random_state=42
)

# Разделение данных
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Создание базовых моделей с предварительным масштабированием
base_models = [
    ('logreg', Pipeline([
        ('scaler', StandardScaler()),
        ('clf', LogisticRegression(max_iter=1000, random_state=42))
    ])),
    ('rf', RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)),
    ('gb', GradientBoostingClassifier(n_estimators=100, max_depth=5, random_state=42)),
    ('svm', Pipeline([
        ('scaler', StandardScaler()),
        ('clf', SVC(probability=True, random_state=42))
    ])),
    ('knn', Pipeline([
        ('scaler', StandardScaler()),
        ('clf', KNeighborsClassifier(n_neighbors=7))
    ]))
]

# Создание мета-модели
meta_model = LogisticRegression(max_iter=1000, random_state=42)

# Создание стекинг-классификатора
stacking_clf = StackingClassifier(
    estimators=base_models,
    final_estimator=meta_model,
    cv=5,
    stack_method='predict_proba',
    passthrough=True,
    n_jobs=-1
)

# Обучение ансамбля
stacking_clf.fit(X_train, y_train)

# Оценка качества
train_score = stacking_clf.score(X_train, y_train)
test_score = stacking_clf.score(X_test, y_test)

print(f"Точность на обучающей выборке: {train_score:.4f}")
print(f"Точность на тестовой выборке: {test_score:.4f}")

# Анализ весов мета-модели
meta_coefs = stacking_clf.final_estimator_.coef_[0]
print(f"Коэффициенты мета-модели: {meta_coefs}")
