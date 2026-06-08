
import tensorflow as tf

from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, Flatten, Dense, Concatenate, Dropout

def build_neural_recommender(n_users, n_items, n_factors=64):
    # Входные слои
    user_input = Input(shape=(1,), name='user_input')
    item_input = Input(shape=(1,), name='item_input')
    
    # Эмбеддинги пользователей и объектов
    user_embedding = Embedding(n_users, n_factors, name='user_embedding')(user_input)
    item_embedding = Embedding(n_items, n_factors, name='item_embedding')(item_input)
    
    # Выравнивание размерности
    user_vec = Flatten()(user_embedding)
    item_vec = Flatten()(item_embedding)
    
    # Объединение представлений
    concat = Concatenate()([user_vec, item_vec])
    
    # Полносвязные слои для нелинейного взаимодействия
    x = Dense(128, activation='relu')(concat)
    x = Dropout(0.3)(x)
    x = Dense(64, activation='relu')(x)
    x = Dropout(0.3)(x)
    x = Dense(32, activation='relu')(x)
    
    # Выходной слой — прогноз оценки
    output = Dense(1, activation='linear', name='rating_output')(x)
    
    model = Model(inputs=[user_input, item_input], outputs=output)
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    return model

# Создание модели
n_users = 10000
n_items = 5000
model = build_neural_recommender(n_users, n_items, n_factors=128)

# Генерация синтетических данных для обучения
sample_size = 50000
user_ids = np.random.randint(0, n_users, size=sample_size)
item_ids = np.random.randint(0, n_items, size=sample_size)
ratings = np.random.randint(1, 6, size=sample_size).astype(np.float32)

# Обучение модели
model.fit(
    [user_ids, item_ids], 
    ratings,
    epochs=10,
    batch_size=256,
    validation_split=0.1,
    verbose=1
)

# Прогнозирование оценки для пары пользователь-объект
test_user = np.array([123])
test_item = np.array([456])
predicted_rating = model.predict([test_user, test_item], verbose=0)
print(f"Прогнозируемая оценка пользователя 123 для объекта 456: {predicted_rating[0][0]:.2f}")
