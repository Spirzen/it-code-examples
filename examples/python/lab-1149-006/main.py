import numpy as np
from openai import OpenAI

client = OpenAI()

def cosine(a, b):
    a, b = np.array(a), np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

texts = [
    "Как вызвать Chat Completions API",
    "REST-запрос к языковой модели",
    "Рецепт борща на кастрюлю",
]

emb = client.embeddings.create(model="text-embedding-3-small", input=texts)
vectors = [item.embedding for item in emb.data]

query_vec = client.embeddings.create(
    model="text-embedding-3-small",
    input="Пример HTTP-вызова OpenAI",
).data[0].embedding

scores = [(t, cosine(query_vec, v)) for t, v in zip(texts, vectors)]
for title, score in sorted(scores, key=lambda x: -x[1]):
    print(f"{score:.3f} — {title}")
