from sklearn.model_selection import cross_val_predict
from sklearn.metrics import accuracy_score

import numpy as np

# Обучение базовых моделей и получение прогнозов для мета-уровня
def generate_meta_features(models, X_train, y_train, X_test, cv=5):
    meta_train = np.zeros((X_train.shape[0], len(models)))
    meta_test = np.zeros((X_test.shape[0], len(models)))
    
    for i, (name, model) in enumerate(models):
        # Кросс-валидационные прогнозы для обучающей выборки
        meta_train[:, i] = cross_val_predict(
            model, X_train, y_train, cv=cv, method='predict_proba'
        )[:, 1]
        
        # Обучение на полной выборке и прогноз для теста
        model.fit(X_train, y_train)
        meta_test[:, i] = model.predict_proba(X_test)[:, 1]
    
    return meta_train, meta_test

# Формирование ансамбля
base_models_list = [
    ('rf', RandomForestClassifier(n_estimators=150, random_state=42)),
    ('gb', GradientBoostingClassifier(n_estimators=150, random_state=42)),
    ('dt', DecisionTreeClassifier(max_depth=15, random_state=42))
]

# Генерация мета-признаков
meta_X_train, meta_X_test = generate_meta_features(
    base_models_list, X_train, y_train, X_test, cv=5
)

# Обучение мета-модели
meta_classifier = LogisticRegression(random_state=42)
meta_classifier.fit(meta_X_train, y_train)

# Прогноз и оценка
meta_predictions = meta_classifier.predict(meta_X_test)
accuracy = accuracy_score(y_test, meta_predictions)

print(f"Точность стекинга: {accuracy:.4f}")
print(f"Коэффициенты мета-модели: {meta_classifier.coef_[0]}")
