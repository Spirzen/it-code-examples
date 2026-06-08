from sklearn.ensemble import RandomForestClassifier
from sklearn.multiclass import OneVsRestClassifier, OneVsOneClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

import numpy as np

# Генерация данных для задачи с 5 классами
X, y = make_classification(
    n_samples=5000,
    n_features=40,
    n_informative=30,
    n_redundant=10,
    n_classes=5,
    n_clusters_per_class=1,
    random_state=42
)

# Разделение данных
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# Базовая модель с нативной поддержкой многоклассовой классификации
base_model = RandomForestClassifier(
    n_estimators=100,
    max_depth=15,
    random_state=42,
    n_jobs=-1
)
base_model.fit(X_train, y_train)
base_pred = base_model.predict(X_test)
base_proba = base_model.predict_proba(X_test)

print("Базовая модель (нативная многоклассовая поддержка):")
print(f"Точность: {accuracy_score(y_test, base_pred):.4f}")
print(classification_report(y_test, base_pred))

# Стратегия один-против-всех
ovr_model = OneVsRestClassifier(
    LogisticRegression(max_iter=1000, random_state=42)
)
ovr_model.fit(X_train, y_train)
ovr_pred = ovr_model.predict(X_test)

print("\nСтратегия один-против-всех:")
print(f"Точность: {accuracy_score(y_test, ovr_pred):.4f}")
print(classification_report(y_test, ovr_pred))

# Стратегия один-против-одного
ovo_model = OneVsOneClassifier(
    LogisticRegression(max_iter=1000, random_state=42)
)
ovo_model.fit(X_train, y_train)
ovo_pred = ovo_model.predict(X_test)

print("\nСтратегия один-против-одного:")
print(f"Точность: {accuracy_score(y_test, ovo_pred):.4f}")
print(classification_report(y_test, ovo_pred))

# Многоклассовая логистическая регрессия с функцией softmax
softmax_model = LogisticRegression(
    multi_class='multinomial',
    solver='lbfgs',
    max_iter=1000,
    random_state=42
)
softmax_model.fit(X_train, y_train)
softmax_pred = softmax_model.predict(X_test)
softmax_proba = softmax_model.predict_proba(X_test)

print("\nМногоклассовая логистическая регрессия (softmax):")
print(f"Точность: {accuracy_score(y_test, softmax_pred):.4f}")
print(classification_report(y_test, softmax_pred))

# Анализ калибровки вероятностей
from sklearn.calibration import calibration_curve

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))

for i in range(5):  # для каждого класса
    fraction_of_positives, mean_predicted_value = calibration_curve(
        (y_test == i).astype(int),
        softmax_proba[:, i],
        n_bins=10
    )
    
    plt.plot(
        mean_predicted_value, 
        fraction_of_positives, 
        marker='o',
        label=f'Класс {i}'
    )

plt.plot([0, 1], [0, 1], 'k--', label='Идеальная калибровка')
plt.xlabel('Среднее предсказанное значение')
plt.ylabel('Доля положительных случаев')
plt.title('Калибровка вероятностей для каждого класса')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('multiclass_calibration.png')
plt.close()

# Важность признаков для каждого класса в логистической регрессии
coef_df = pd.DataFrame(
    softmax_model.coef_,
    index=[f'Класс_{i}' for i in range(5)],
    columns=[f'feature_{j}' for j in range(40)]
)

print("\nТоп-5 важных признаков для каждого класса (логистическая регрессия):")
for class_idx in range(5):
    top_features = coef_df.loc[f'Класс_{class_idx}'].abs().nlargest(5)
    print(f"\nКласс {class_idx}:")
    for feature, importance in top_features.items():
        raw_coef = coef_df.loc[f'Класс_{class_idx}', feature]
        direction = "положительное" if raw_coef > 0 else "отрицательное"
        print(f"  {feature}: {importance:.4f} ({direction} влияние)")
