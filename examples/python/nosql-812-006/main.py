
import torch
import chromadb

from chromadb.utils import embedding_functions

class КэшированныйКлассификатор:
    def __init__(self, модель, порог_сходства=0.95):
        self.модель = модель
        self.порог_сходства = порог_сходства
        
        # Инициализация векторной базы
        клиент = chromadb.Client()
        функция_эмбеддингов = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )
        
        self.коллекция = клиент.create_collection(
            name="кэш_классификации",
            embedding_function=функция_эмбеддингов
        )
    
    def предсказать(self, входной_текст):
        # Получение эмбеддинга запроса
        эмбеддинг = self.коллекция._embedding_function([входной_текст])[0]
        
        # Поиск похожих записей в кэше
        результаты = self.коллекция.query(
            query_embeddings=[эмбеддинг],
            n_results=1
        )
        
        # Проверка сходства
        if результаты['distances'][0] and результаты['distances'][0][0] < (1 - self.порог_сходства):
            # Возврат закэшированного результата
            return результаты['metadatas'][0][0]['предсказание']
        
        # Запуск модели при отсутствии подходящего кэша
        с_отключённым_градиентом = torch.no_grad()
        with с_отключённым_градиентом:
            тензор = токенизатор(входной_текст, return_tensors="pt")
            выход = self.модель(**тензор)
            предсказание = torch.argmax(выход.logits, dim=1).item()
        
        # Сохранение результата в кэш
        self.коллекция.add(
            documents=[входной_текст],
            embeddings=[эмбеддинг],
            metadatas=[{"предсказание": предсказание}],
            ids=[f"id_{hash(входной_текст)}"]
        )
        
        return предсказание
