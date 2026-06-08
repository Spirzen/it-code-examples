from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

import numpy as np

class ActiveLearningSystem:
    def __init__(self, model, strategy='uncertainty'):
        self.model = model
        self.strategy = strategy
        self.X_labeled = None
        self.y_labeled = None
        self.X_pool = None
        self.y_pool_true = None
    
    def initialize(self, X_labeled, y_labeled, X_pool, y_pool_true):
        self.X_labeled = X_labeled.copy()
        self.y_labeled = y_labeled.copy()
        self.X_pool = X_pool.copy()
        self.y_pool_true = y_pool_true.copy()
    
    def query_uncertainty(self, n_queries):
        probabilities = self.model.predict_proba(self.X_pool)
        uncertainties = 1 - np.max(probabilities, axis=1)
        query_indices = np.argsort(uncertainties)[-n_queries:][::-1]
        return query_indices
    
    def query_margin(self, n_queries):
        probabilities = self.model.predict_proba(self.X_pool)
        sorted_probs = np.sort(probabilities, axis=1)
        margins = sorted_probs[:, -1] - sorted_probs[:, -2]
        query_indices = np.argsort(margins)[:n_queries]
        return query_indices
    
    def query_entropy(self, n_queries):
        probabilities = self.model.predict_proba(self.X_pool)
        probabilities = np.clip(probabilities, 1e-10, 1.0)
        entropy = -np.sum(probabilities * np.log2(probabilities), axis=1)
        query_indices = np.argsort(entropy)[-n_queries:][::-1]
        return query_indices
    
    def query(self, n_queries):
        if self.strategy == 'uncertainty':
            indices = self.query_uncertainty(n_queries)
        elif self.strategy == 'margin':
            indices = self.query_margin(n_queries)
        elif self.strategy == 'entropy':
            indices = self.query_entropy(n_queries)
        else:
            raise ValueError(f"Неизвестная стратегия: {self.strategy}")
        
        return indices
    
    def update(self, query_indices):
        # Получение истинных меток из пула
        new_X = self.X_pool[query_indices]
        new_y = self.y_pool_true[query_indices]
        
        # Добавление в размеченный набор
        self.X_labeled = np.vstack([self.X_labeled, new_X])
        self.y_labeled = np.hstack([self.y_labeled, new_y])
        
        # Удаление из пула
        mask = np.ones(len(self.X_pool), dtype=bool)
        mask[query_indices] = False
        self.X_pool = self.X_pool[mask]
        self.y_pool_true = self.y_pool_true[mask]
    
    def train(self):
        self.model.fit(self.X_labeled, self.y_labeled)

# Генерация данных для демонстрации
X, y = make_classification(
    n_samples=5000,
    n_features=50,
    n_informative=30,
    n_redundant=20,
    n_classes=3,
    random_state=42
)

# Разделение на начальный размеченный набор и пул для запросов
X_init, X_pool, y_init, y_pool = train_test_split(
    X, y, train_size=50, stratify=y, random_state=42
)

# Инициализация системы активного обучения
model = RandomForestClassifier(n_estimators=100, random_state=42)
al_system = ActiveLearningSystem(model, strategy='uncertainty')
al_system.initialize(X_init, y_init, X_pool, y_pool)

# Цикл активного обучения
n_iterations = 30
queries_per_iteration = 10
accuracy_history = []

for iteration in range(n_iterations):
    # Обучение модели
    al_system.train()
    
    # Оценка качества на всём исходном наборе данных
    accuracy = al_system.model.score(X, y)
    accuracy_history.append(accuracy)
    
    print(f"Итерация {iteration}: размечено {len(al_system.X_labeled)} объектов, "
          f"точность {accuracy:.4f}")
    
    # Запрос новых объектов для разметки
    if len(al_system.X_pool) >= queries_per_iteration:
        query_indices = al_system.query(queries_per_iteration)
        al_system.update(query_indices)
    else:
        break

# Сравнение с пассивным обучением
passive_accuracies = []
X_passive_labeled = X_init.copy()
y_passive_labeled = y_init.copy()
X_passive_pool = X_pool.copy()
y_passive_pool = y_pool.copy()

for iteration in range(n_iterations):
    model_passive = RandomForestClassifier(n_estimators=100, random_state=42)
    model_passive.fit(X_passive_labeled, y_passive_labeled)
    accuracy = model_passive.score(X, y)
    passive_accuracies.append(accuracy)
    
    # Случайный выбор объектов для разметки
    if len(X_passive_pool) >= queries_per_iteration:
        random_indices = np.random.choice(
            len(X_passive_pool), 
            queries_per_iteration, 
            replace=False
        )
        X_passive_labeled = np.vstack([X_passive_labeled, X_passive_pool[random_indices]])
        y_passive_labeled = np.hstack([y_passive_labeled, y_passive_pool[random_indices]])
        
        mask = np.ones(len(X_passive_pool), dtype=bool)
        mask[random_indices] = False
        X_passive_pool = X_passive_pool[mask]
        y_passive_pool = y_passive_pool[mask]

# Визуализация эффективности активного обучения
plt.figure(figsize=(12, 6))
labeled_counts = np.arange(len(accuracy_history)) * queries_per_iteration + len(X_init)
plt.plot(labeled_counts, accuracy_history, 'b-o', label='Активное обучение (неопределённость)', linewidth=2)
plt.plot(labeled_counts, passive_accuracies, 'r--s', label='Пассивное обучение (случайный выбор)', linewidth=2)
plt.xlabel('Количество размеченных объектов')
plt.ylabel('Точность на полном наборе данных')
plt.title('Эффективность активного обучения')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('active_learning_efficiency.png')
plt.close()
