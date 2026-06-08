
import implicit
import numpy as np

from scipy.sparse import csr_matrix

# Генерация синтетических данных о взаимодействиях
np.random.seed(42)
n_users = 1000
n_items = 500
density = 0.05

# Создание разреженной матрицы взаимодействий
interactions = np.random.choice(
    [0, 1, 2, 3, 4, 5], 
    size=(n_users, n_items), 
    p=[0.95, 0.01, 0.01, 0.01, 0.01, 0.01]
)
interactions_matrix = csr_matrix(interactions)

# Обучение модели ALS (Alternating Least Squares)
model = implicit.als.AlternatingLeastSquares(
    factors=50,
    regularization=0.01,
    iterations=15,
    calculate_training_loss=True,
    random_state=42
)

# Обучение на данных (необходимо преобразование для implicit)
model.fit(interactions_matrix.T)  # implicit ожидает матрицу объекты×пользователи

# Получение рекомендаций для пользователя
user_id = 42
user_items = interactions_matrix[user_id]
recommendations = model.recommend(user_id, user_items, N=10)

print(f"Рекомендации для пользователя {user_id}:")
for item_id, score in recommendations:
    print(f"  Объект {item_id}: оценка {score:.4f}")

# Поиск похожих объектов
item_id = 100
similar_items = model.similar_items(item_id, N=5)
print(f"\nОбъекты, похожие на объект {item_id}:")
for similar_id, score in similar_items:
    print(f"  Объект {similar_id}: сходство {score:.4f}")
