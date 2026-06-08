
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout, Bidirectional
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

import numpy as np

# Генерация синтетического текстового корпуса
texts = [
    "отличный продукт рекомендую всем",
    "ужасное качество не покупайте",
    "нормально но дорого",
    "восхитительно превзошло ожидания",
    "полное разочарование деньги на ветер",
    "хорошо работает без нареканий",
    "кошмарный опыт никогда больше",
    "среднее качество за эти деньги",
    "просто замечательно всем доволен",
    "отвратительно не соответствует описанию"
] * 100  # повторение для увеличения объёма данных

labels = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0] * 100  # 1 - позитив, 0 - негатив

# Токенизация и векторизация текста
max_words = 1000
max_len = 20

tokenizer = Tokenizer(num_words=max_words, oov_token="<OOV>")
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)
padded_sequences = pad_sequences(sequences, maxlen=max_len, padding='post')

# Разделение данных
split_idx = int(len(padded_sequences) * 0.8)
X_train = padded_sequences[:split_idx]
y_train = np.array(labels[:split_idx])
X_test = padded_sequences[split_idx:]
y_test = np.array(labels[split_idx:])

# Построение модели с двунаправленным LSTM
model = Sequential([
    Embedding(input_dim=max_words, output_dim=64, input_length=max_len),
    Bidirectional(LSTM(64, return_sequences=True)),
    Dropout(0.3),
    Bidirectional(LSTM(32)),
    Dropout(0.3),
    Dense(24, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Компиляция и обучение
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

model.fit(
    X_train, y_train,
    epochs=10,
    batch_size=32,
    validation_split=0.1,
    verbose=1
)

# Оценка качества
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Точность на тестовой выборке: {accuracy:.4f}")

# Прогнозирование новых текстов
new_texts = ["отличное качество и быстрая доставка", "ужасная поддержка клиентов"]
new_sequences = tokenizer.texts_to_sequences(new_texts)
new_padded = pad_sequences(new_sequences, maxlen=max_len, padding='post')
predictions = model.predict(new_padded)

for text, pred in zip(new_texts, predictions):
    sentiment = "позитивный" if pred[0] > 0.5 else "негативный"
    print(f"'{text}' -> {sentiment} (уверенность {pred[0]:.2%})")
