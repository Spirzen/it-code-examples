from imblearn.over_sampling import SMOTE, ADASYN
from imblearn.under_sampling import RandomUnderSampler
from imblearn.combine import SMOTETomek
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.datasets import make_classification

import numpy as np

# Генерация сильно несбалансированных данных
X, y = make_classification(
    n_samples=10000,
    n_features=50,
    n_informative=30,
    n_redundant=20,
    n_classes=2,
    weights=[0.98, 0.02],  # 98% негативных, 2% позитивных
    flip_y=0.01,
    random_state=42
)

# Разделение данных
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

print(f"Распределение классов в обучающей выборке: {np.bincount(y_train)}")
print(f"Распределение классов в тестовой выборке: {np.bincount(y_test)}")

# Базовая модель без обработки дисбаланса
base_model = RandomForestClassifier(n_estimators=100, random_state=42)
base_model.fit(X_train, y_train)
base_pred = base_model.predict(X_test)
base_proba = base_model.predict_proba(X_test)[:, 1]

print("\nБазовая модель (без обработки дисбаланса):")
print(classification_report(y_test, base_pred))
print(f"ROC-AUC: {roc_auc_score(y_test, base_proba):.4f}")

# Применение SMOTE
smote = SMOTE(sampling_strategy=0.5, k_neighbors=5, random_state=42)
X_smote, y_smote = smote.fit_resample(X_train, y_train)

print(f"\nПосле SMOTE: {np.bincount(y_smote)}")

smote_model = RandomForestClassifier(n_estimators=100, random_state=42)
smote_model.fit(X_smote, y_smote)
smote_pred = smote_model.predict(X_test)
smote_proba = smote_model.predict_proba(X_test)[:, 1]

print("\nМодель после SMOTE:")
print(classification_report(y_test, smote_pred))
print(f"ROC-AUC: {roc_auc_score(y_test, smote_proba):.4f}")

# Применение комбинированного метода SMOTETomek
smt = SMOTETomek(sampling_strategy=0.5, random_state=42)
X_smt, y_smt = smt.fit_resample(X_train, y_train)

print(f"\nПосле SMOTETomek: {np.bincount(y_smt)}")

smt_model = RandomForestClassifier(n_estimators=100, random_state=42)
smt_model.fit(X_smt, y_smt)
smt_pred = smt_model.predict(X_test)
smt_proba = smt_model.predict_proba(X_test)[:, 1]

print("\nМодель после SMOTETomek:")
print(classification_report(y_test, smt_pred))
print(f"ROC-AUC: {roc_auc_score(y_test, smt_proba):.4f}")

# Взвешивание классов без изменения данных
weighted_model = RandomForestClassifier(
    n_estimators=100,
    class_weight='balanced',
    random_state=42
)
weighted_model.fit(X_train, y_train)
weighted_pred = weighted_model.predict(X_test)
weighted_proba = weighted_model.predict_proba(X_test)[:, 1]

print("\nМодель с взвешиванием классов:")
print(classification_report(y_test, weighted_pred))
print(f"ROC-AUC: {roc_auc_score(y_test, weighted_proba):.4f}")

# Оптимизация порога классификации
from sklearn.metrics import precision_recall_curve

precision, recall, thresholds = precision_recall_curve(y_test, smote_proba)
f1_scores = 2 * (precision * recall) / (precision + recall + 1e-10)
optimal_idx = np.argmax(f1_scores[:-1])  # исключаем последний элемент
optimal_threshold = thresholds[optimal_idx]

print(f"\nОптимальный порог классификации: {optimal_threshold:.3f}")
print(f"Максимальная F1-мера при этом пороге: {f1_scores[optimal_idx]:.4f}")

# Применение оптимального порога
optimized_pred = (smote_proba >= optimal_threshold).astype(int)
print("\nМодель с оптимизированным порогом:")
print(classification_report(y_test, optimized_pred))
