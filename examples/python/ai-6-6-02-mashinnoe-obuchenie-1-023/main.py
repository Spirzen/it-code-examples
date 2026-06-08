
import tensorflow as tf

from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout, Bidirectional
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# Параметры
max_features = 20000
maxlen = 200
embedding_dim = 128

# Загружаем данные
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=max_features)

# Дополняем последовательности до одинаковой длины
X_train = pad_sequences(X_train, maxlen=maxlen)
X_test = pad_sequences(X_test, maxlen=maxlen)

# Создаем модель
model = Sequential([
    Embedding(max_features, embedding_dim, input_length=maxlen),
    Bidirectional(LSTM(64, return_sequences=True)),
    Dropout(0.5),
    Bidirectional(LSTM(32)),
    Dropout(0.5),
    Dense(64, activation='relu'),
    Dropout(0.5),
    Dense(1, activation='sigmoid')
])

# Компилируем модель
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy', tf.keras.metrics.Precision(), tf.keras.metrics.Recall()]
)

# Callbacks
callbacks = [
    EarlyStopping(patience=5, restore_best_weights=True),
    ModelCheckpoint('sentiment_model.h5', save_best_only=True)
]

# Обучаем модель
history = model.fit(
    X_train, y_train,
    epochs=15,
    batch_size=128,
    validation_split=0.2,
    callbacks=callbacks
)

# Оцениваем модель
loss, accuracy, precision, recall = model.evaluate(X_test, y_test)
print(f"Точность: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")

# Предсказание для нового текста
def predict_sentiment(text, word_index):
    # Преобразуем текст в последовательность индексов
    sequence = []
    for word in text.lower().split():
        if word in word_index and word_index[word] < max_features:
            sequence.append(word_index[word])
    
    # Дополняем последовательность
    sequence = pad_sequences([sequence], maxlen=maxlen)
    
    # Предсказываем
    prediction = model.predict(sequence)[0][0]
    return prediction

# Пример использования
sample_text = "This movie was absolutely fantastic and I loved every minute of it!"
# prediction = predict_sentiment(sample_text, imdb.get_word_index())
# print(f"Sentiment score — {prediction:.4f} ({'Positive' if prediction > 0.5 else 'Negative'})")
