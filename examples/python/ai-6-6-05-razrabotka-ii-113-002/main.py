
import os

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Загрузка документов из папки
loader = DirectoryLoader("my_project/", glob="**/*.md", show_progress=True)
docs = loader.load()

# Разбиение на чанки
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=512,
    chunk_overlap=50,
    length_function=len,
)
chunks = text_splitter.split_documents(docs)

# Локальная модель эмбеддингов
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cuda"},  # или "cpu"
)

# Создание и сохранение векторного хранилища
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"
)
vectorstore.persist()
print("Индексация завершена. База сохранена в ./chroma_db")
