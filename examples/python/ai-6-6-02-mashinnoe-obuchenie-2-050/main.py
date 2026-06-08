from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import numpy as np

class SelfTrainingClassifier:
    def __init__(self, base_classifier, threshold=0.75, max_iterations=10):
        self.base_classifier = base_classifier
        self.threshold = threshold
        self.max_iterations = max_iterations
        self.X_labeled = None
        self.y_labeled = None
        self.X_unlabeled = None
    
    def fit(self, X_labeled, y_labeled, X_unlabeled):
        self.X_labeled = X_labeled.copy()
        self.y_labeled = y_labeled.copy()
        self.X_unlabeled = X_unlabeled.copy()
        
        for iteration in range(self.max_iterations):
            # Обучение на текущем размеченном наборе
            self.base_classifier.fit(self.X_labeled, self.y_labeled)
            
            # Прогнозирование на неразмеченных данных
            probabilities = self.base_classifier.predict_proba(self.X_unlabeled)
            max_probs = np.max(probabilities, axis=1)
            predictions = np.argmax(probabilities, axis=1)
            
            # Выбор объектов для псевдоразметки
            mask = max_probs >= self.threshold
            n_new = np.sum(mask)
            
            if n_new == 0:
                print(f"Итерация {iteration}: нет объектов с уверенностью выше порога {self.threshold:.2f}")
                break
            
            # Добавление псевдоразмеченных объектов
            new_X = self.X_unlabeled[mask]
            new_y = predictions[mask]
            
            self.X_labeled = np.vstack([self.X_labeled, new_X])
            self.y_labeled = np.hstack([self.y_labeled, new_y])
            
            # Удаление из неразмеченного пула
            self.X_unlabeled = self.X_unlabeled[~mask]
            
            print(f"Итерация {iteration}: добавлено {n_new} псевдоразмеченных объектов, "
                  f"всего размечено {len(self.X_labeled)}, осталось неразмеченных {len(self.X_unlabeled)}")
            
            if len(self.X_unlabeled) == 0:
                break
        
        # Финальное обучение на расширенном наборе
        self.base_classifier.fit(self.X_labeled, self.y_labeled)
        return self
    
    def predict(self, X):
        return self.base_classifier.predict(X)
    
    def predict_proba(self, X):
        return self.base_classifier.predict_proba(X)

# Генерация данных с большим объёмом неразмеченных примеров
X, y = make_classification(
    n_samples=10000,
    n_features=100,
    n_informative=50,
    n_redundant=50,
    n_classes=5,
    random_state=42
)

# Разделение — 50 размеченных, 9950 неразмеченных
X_labeled, X_unlabeled, y_labeled, y_unlabeled = train_test_split(
    X, y, train_size=50, stratify=y, random_state=42
)

# Базовый классификатор
base_clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Обучение самообучающегося классификатора
self_training_clf = SelfTrainingClassifier(
    base_classifier=base_clf,
    threshold=0.85,
    max_iterations=15
)
self_training_clf.fit(X_labeled, y_labeled, X_unlabeled)

# Оценка качества
final_accuracy = accuracy_score(y, self_training_clf.predict(X))
print(f"\nФинальная точность после самообучения: {final_accuracy:.4f}")

# Сравнение с обучением только на начальных 50 примерах
base_clf.fit(X_labeled, y_labeled)
baseline_accuracy = accuracy_score(y, base_clf.predict(X))
print(f"Точность без самообучения (50 примеров): {baseline_accuracy:.4f}")

# Сравнение с обучением на всех 10000 размеченных примерах
full_clf = RandomForestClassifier(n_estimators=100, random_state=42)
full_clf.fit(X, y)
full_accuracy = accuracy_score(y, full_clf.predict(X))
print(f"Точность при полной разметке (10000 примеров): {full_accuracy:.4f}")
