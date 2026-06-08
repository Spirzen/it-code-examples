
import chromadb

from chromadb.utils import embedding_functions

# Создание клиента
client = chromadb.PersistentClient(path="/путь/к/хранилищу")

# Выбор функции эмбеддингов
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# Создание коллекции
collection = client.create_collection(
    name="документы",
    embedding_function=embedding_function,
    metadata={"hnsw:space": "cosine"}  # косинусное сходство
)

# Добавление документов
collection.add(
    documents=["Кошки спят большую часть дня", "Собаки любят гулять"],
    metadatas=[{"категория": "животные"}, {"категория": "животные"}],
    ids=["id1", "id2"]
)

# Поиск похожих документов
результаты = collection.query(
    query_texts=["Домашние питомцы и их привычки"],
    n_results=2,
    where={"категория": "животные"}  # фильтр по метаданным
)
