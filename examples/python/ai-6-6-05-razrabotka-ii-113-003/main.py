from openai import OpenAI
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# Подключение к векторной базе
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cuda"}
)
vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)

# Поиск релевантных фрагментов
query = "Как настроить подключение к PostgreSQL?"
retrieved = vectorstore.similarity_search(query, k=3)
context = "\n\n".join([doc.page_content for doc in retrieved])

# Формирование промпта
prompt = f"""Ответь на вопрос, используя только предоставленный контекст.
Если в контексте нет нужной информации, скажи: "Я не знаю".

Контекст:
{context}

Вопрос: {query}
Ответ:"""

# Запрос к локальной модели через OpenAI-совместимый API
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")
response = client.chat.completions.create(
    model="llama3",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.2,  # низкая температура для точности
    max_tokens=512
)

print(response.choices[0].message.content)
