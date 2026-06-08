from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from collections import defaultdict

class HierarchicalClassifier:
    def __init__(self):
        self.hierarchy = defaultdict(dict)
        self.models = {}
    
    def define_hierarchy(self, categories):
        """
        Определение иерархии категорий.
        Формат: {родитель: [потомок1, потомок2, ...]}
        """
        self.hierarchy = categories
    
    def fit(self, X, y_path):
        """
        Обучение иерархической модели.
        y_path: список путей к листовым категориям для каждого объекта
        Пример пути: ['электроника', 'мобильные_устройства', 'смартфоны']
        """
        # Группировка объектов по уровням иерархии
        level_data = defaultdict(lambda: defaultdict(list))
        
        for idx, path in enumerate(y_path):
            for level, category in enumerate(path):
                level_data[level][category].append(idx)
        
        # Обучение моделей для каждого узла иерархии
        for level in sorted(level_data.keys()):
            categories_at_level = list(level_data[level].keys())
            
            if level == 0:
                # Корневой уровень — обучение на всех данных
                X_level = X
                y_level = [next((cat for cat in categories_at_level 
                               if idx in level_data[level][cat]), None)
                         for idx in range(len(X))]
                self.models['root'] = RandomForestClassifier(
                    n_estimators=50, 
                    max_depth=10,
                    random_state=42
                )
                self.models['root'].fit(X_level, y_level)
            else:
                # Обучение моделей для каждого родительского узла
                parent_level = level - 1
                for parent_cat in level_data[parent_level].keys():
                    # Сбор данных для потомков данного родителя
                    child_indices = []
                    child_labels = []
                    
                    for child_cat in categories_at_level:
                        indices = level_data[level][child_cat]
                        # Фильтрация объектов, принадлежащих этому родителю
                        valid_indices = [idx for idx in indices 
                                       if idx in level_data[parent_level][parent_cat]]
                        if valid_indices:
                            child_indices.extend(valid_indices)
                            child_labels.extend([child_cat] * len(valid_indices))
                    
                    if child_indices:
                        X_child = X[child_indices]
                        model_key = f"{parent_cat}_level_{level}"
                        self.models[model_key] = DecisionTreeClassifier(
                            max_depth=8,
                            random_state=42
                        )
                        self.models[model_key].fit(X_child, child_labels)
    
    def predict(self, X):
        """
        Прогнозирование полного пути категорий для объектов.
        Возвращает список путей той же длины, что и X.
        """
        predictions = []
        
        for x in X:
            path = []
            current_node = 'root'
            current_x = x.reshape(1, -1)
            
            while current_node in self.models:
                model = self.models[current_node]
                pred = model.predict(current_x)[0]
                path.append(pred)
                
                # Формирование ключа для следующего уровня
                next_node = f"{pred}_level_{len(path)}"
                if next_node in self.models:
                    current_node = next_node
                else:
                    break
            
            predictions.append(path)
        
        return predictions

# Пример использования с синтетическими данными таксономии
np.random.seed(42)

# Определение иерархии категорий товаров
taxonomy = {
    'root': ['электроника', 'одежда', 'книги'],
    'электроника': ['мобильные_устройства', 'компьютеры', 'аудиотехника'],
    'мобильные_устройства': ['смартфоны', 'планшеты'],
    'компьютеры': ['ноутбуки', 'настольные_пк'],
    'одежда': ['верхняя_одежда', 'обувь'],
    'верхняя_одежда': ['куртки', 'пальто'],
    'книги': ['художественные', 'технические']
}

# Генерация синтетических признаков для товаров
n_samples = 1000
n_features = 30
X = np.random.randn(n_samples, n_features)

# Генерация путей категорий
category_paths = []
for _ in range(n_samples):
    path = ['электроника']
    if np.random.rand() < 0.5:
        path.append('мобильные_устройства')
        path.append('смартфоны' if np.random.rand() < 0.7 else 'планшеты')
    else:
        path.append('компьютеры')
        path.append('ноутбуки' if np.random.rand() < 0.6 else 'настольные_пк')
    category_paths.append(path)

# Создание и обучение иерархического классификатора
hierarchical_clf = HierarchicalClassifier()
hierarchical_clf.define_hierarchy(taxonomy)
hierarchical_clf.fit(X, category_paths)

# Прогнозирование для новых объектов
test_X = np.random.randn(5, n_features)
predictions = hierarchical_clf.predict(test_X)

print("Прогнозируемые категории для тестовых объектов:")
for i, pred_path in enumerate(predictions):
    print(f"Объект {i}: {' -> '.join(pred_path)}")
