from transformers import BertTokenizer, BertModel

import torch

# Загрузка токенизатора и модели
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Подготовка текста
text = "Машинное обучение преобразует современные технологии"
inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True, max_length=128)

# Получение эмбеддингов
with torch.no_grad():
    outputs = model(**inputs)
    last_hidden_states = outputs.last_hidden_state

# Эмбеддинг предложения как среднее по токенам
sentence_embedding = last_hidden_states.mean(dim=1)
print(f"Размерность эмбеддинга предложения: {sentence_embedding.shape}")

# Эмбеддинги отдельных токенов
tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])
for i, token in enumerate(tokens):
    if token not in ['[CLS]', '[SEP]', '[PAD]']:
        token_embedding = last_hidden_states[0, i]
        print(f"Токен '{token}': вектор размерности {token_embedding.shape}")
