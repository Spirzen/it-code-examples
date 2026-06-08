from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.metrics import confusion_matrix, classification_report

import numpy as np

# Пример оценки модели
y_true = np.array([0, 1, 1, 0, 1, 0, 1, 1, 0, 1])
y_pred = np.array([0, 1, 0, 0, 1, 0, 1, 1, 1, 1])
y_proba = np.array([0.1, 0.9, 0.4, 0.2, 0.8, 0.3, 0.9, 0.85, 0.6, 0.95])

# Вычисляем метрики
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)
roc_auc = roc_auc_score(y_true, y_proba)

print(f"Точность: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-score: {f1:.2f}")
print(f"ROC-AUC: {roc_auc:.2f}")

# Матрица ошибок
cm = confusion_matrix(y_true, y_pred)
print("\nМатрица ошибок:")
print(cm)

# Подробный отчет
report = classification_report(y_true, y_pred)
print("\nОтчет классификации:")
print(report)
