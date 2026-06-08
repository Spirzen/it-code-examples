from pinecone import Pinecone, ServerlessSpec

# Инициализация клиента
pc = Pinecone(api_key="ваш_ключ_api")

# Создание индекса
pc.create_index(
    name="мой-индекс",
    dimension=384,
    metric="cosine",
    spec=ServerlessSpec(cloud="aws", region="us-west-2")
)

# Получение ссылки на индекс
index = pc.Index("мой-индекс")

# Загрузка векторов
index.upsert(
    vectors=[
        ("вектор-1", [0.1, 0.2, 0.3, ...], {"категория": "текст"}),
        ("вектор-2", [0.4, 0.5, 0.6, ...], {"категория": "текст"})
    ]
)

# Поиск
результат = index.query(
    vector=[0.15, 0.25, 0.35, ...],
    top_k=3,
    filter={"категория": {"$eq": "текст"}}
)
