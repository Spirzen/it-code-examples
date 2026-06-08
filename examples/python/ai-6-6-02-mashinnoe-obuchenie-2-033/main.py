from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import GradientBoostingClassifier
from scipy.stats import randint, uniform

import numpy as np

# Генерация данных
X, y = make_classification(
    n_samples=5000,
    n_features=50,
    n_informative=35,
    n_redundant=15,
    random_state=42
)

# Модель
clf = GradientBoostingClassifier(random_state=42)

# Пространство поиска гиперпараметров
param_dist = {
    'n_estimators': randint(50, 300),
    'max_depth': randint(3, 10),
    'learning_rate': uniform(0.01, 0.2),
    'min_samples_split': randint(2, 20),
    'min_samples_leaf': randint(1, 10),
    'subsample': uniform(0.7, 0.3),
    'max_features': ['sqrt', 'log2', None]
}

# Настройка случайного поиска
random_search = RandomizedSearchCV(
    estimator=clf,
    param_distributions=param_dist,
    n_iter=50,
    cv=5,
    scoring='roc_auc',
    random_state=42,
    n_jobs=-1,
    verbose=1
)

# Выполнение поиска
random_search.fit(X, y)

# Результаты
print(f"Лучшая оценка ROC-AUC: {random_search.best_score_:.4f}")
print(f"Лучшие параметры: {random_search.best_params_}")

# Анализ важности параметров
cv_results = random_search.cv_results_
for param in param_dist.keys():
    if param in cv_results:
        print(f"\nВлияние параметра {param}:")
        # Вывод топ-3 комбинаций по этому параметру
        indices = np.argsort(cv_results['mean_test_score'])[-3:][::-1]
        for idx in indices:
            print(f"  Значение {cv_results['param_' + param][idx]}: оценка {cv_results['mean_test_score'][idx]:.4f}")
