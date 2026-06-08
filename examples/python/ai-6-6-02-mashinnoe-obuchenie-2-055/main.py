
import shap
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt

# Генерация данных
X, y = make_classification(
    n_samples=5000,
    n_features=20,
    n_informative=15,
    n_redundant=5,
    random_state=42
)

feature_names = [f'feature_{i}' for i in range(20)]

# Разделение данных
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Обучение модели
model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
model.fit(X_train, y_train)

# Создание эксплайнера SHAP
explainer = shap.TreeExplainer(model)

# Вычисление значений Шепли для тестовой выборки
shap_values = explainer.shap_values(X_test)

# Визуализация важности признаков (глобальная интерпретация)
plt.figure(figsize=(12, 8))
shap.summary_plot(
    shap_values[1], 
    X_test, 
    feature_names=feature_names,
    plot_type="bar",
    show=False
)
plt.title('Глобальная важность признаков (значения Шепли)')
plt.tight_layout()
plt.savefig('shap_global_importance.png')
plt.close()

# Визуализация распределения влияния признаков
plt.figure(figsize=(12, 8))
shap.summary_plot(
    shap_values[1], 
    X_test, 
    feature_names=feature_names,
    show=False
)
plt.title('Распределение влияния признаков на прогнозы')
plt.tight_layout()
plt.savefig('shap_summary_plot.png')
plt.close()

# Интерпретация отдельного прогноза
sample_idx = 42
sample = X_test[sample_idx:sample_idx+1]

plt.figure(figsize=(10, 6))
shap.waterfall_plot(
    shap.Explanation(
        values=shap_values[1][sample_idx], 
        base_values=explainer.expected_value[1],
        data=sample[0],
        feature_names=feature_names
    )
)
plt.title(f'Объяснение прогноза для объекта {sample_idx}')
plt.tight_layout()
plt.savefig('shap_waterfall.png')
plt.close()

# Силовые графики для нескольких объектов
plt.figure(figsize=(12, 10))
shap.force_plot(
    explainer.expected_value[1],
    shap_values[1][:50, :],
    X_test[:50, :],
    feature_names=feature_names,
    matplotlib=True,
    show=False
)
plt.title('Силовые графики для 50 объектов')
plt.tight_layout()
plt.savefig('shap_force_plot.png')
plt.close()

# Зависимость прогноза от двух ключевых признаков
plt.figure(figsize=(12, 5))
shap.dependence_plot(
    0,  # индекс первого признака
    shap_values[1],
    X_test,
    feature_names=feature_names,
    interaction_index=1,  # взаимодействие с вторым признаком
    show=False
)
plt.title('Зависимость влияния признака 0 от значения признака 1')
plt.tight_layout()
plt.savefig('shap_dependence_plot.png')
plt.close()
