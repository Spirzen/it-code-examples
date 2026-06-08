from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.datasets import make_classification

# Генерация данных
X, y = make_classification(
    n_samples=1000,
    n_features=20,
    n_informative=15,
    n_redundant=5,
    random_state=42
)

# Создание конвейера
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('logreg', LogisticRegression(
        penalty='l2',
        C=1.0,
        solver='lbfgs',
        max_iter=100,
        multi_class='auto',
        class_weight=None,
        random_state=42
    ))
])

# Обучение модели
pipeline.fit(X, y)

# Получение коэффициентов модели
coefficients = pipeline.named_steps['logreg'].coef_
intercept = pipeline.named_steps['logreg'].intercept_
