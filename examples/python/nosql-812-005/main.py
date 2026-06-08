from pymilvus import (
    connections, 
    Collection,
    DataType,
    FieldSchema,
    CollectionSchema
)

# Подключение к кластеру
connections.connect("default", host="localhost", port="19530")

# Определение схемы коллекции
fields = [
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
    FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=768),
    FieldSchema(name="категория", dtype=DataType.VARCHAR, max_length=100),
    FieldSchema(name="дата_создания", dtype=DataType.INT64),
    FieldSchema(name="язык", dtype=DataType.VARCHAR, max_length=10)
]

schema = CollectionSchema(fields, "коллекция_документов")
коллекция = Collection("документы", schema)

# Создание индекса для векторного поля
коллекция.create_index(
    field_name="vector",
    index_params={
        "index_type": "HNSW",
        "metric_type": "COSINE",
        "params": {"M": 16, "efConstruction": 200}
    }
)

# Поиск с фильтрацией по метаданным
результаты = коллекция.search(
    data=[[0.1, 0.2, 0.3, ...]],  # вектор запроса
    anns_field="vector",
    param={
        "metric_type": "COSINE",
        "params": {"ef": 50}
    },
    limit=10,
    expr='категория == "техническая_документация" && дата_создания >= 1704067200'
)
