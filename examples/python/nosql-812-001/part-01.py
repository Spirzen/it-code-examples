from sentence_transformers import SentenceTransformer

# Загрузка предобученной модели
model = SentenceTransformer('all-MiniLM-L6-v2')

# Векторизация списка предложений
sentences = [
    "Кошки спят большую часть дня",
    "Собаки любят гулять на улице",
    "Кошки охотятся на мелких грызунов"
]

# Получение эмбеддингов
embeddings = model.encode(sentences)

# embeddings.shape вернёт (3, 384) — три вектора размерностью 384
print(f"Размерность векторов: {embeddings.shape[1]}")
