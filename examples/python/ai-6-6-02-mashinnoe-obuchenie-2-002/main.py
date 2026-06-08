from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

# Загрузка данных
iris = load_iris()
X, y = iris.data, iris.target

# Создание и обучение модели
clf = DecisionTreeClassifier(
    criterion='gini',
    max_depth=3,
    min_samples_split=2,
    random_state=42
)
clf.fit(X, y)

# Визуализация структуры дерева
from sklearn.tree import export_text
tree_rules = export_text(clf, feature_names=iris.feature_names)
print(tree_rules)
