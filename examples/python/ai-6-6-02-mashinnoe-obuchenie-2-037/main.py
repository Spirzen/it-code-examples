from transformers import BertTokenizer, BertForSequenceClassification

import torch.nn.functional as F

# Загрузка модели для классификации
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained(
    'bert-base-uncased', 
    num_labels=3  # три класса: позитивный, нейтральный, негативный
)

# Подготовка нескольких текстов
texts = [
    "Отличный продукт, очень доволен покупкой",
    "Товар пришёл повреждённым, разочарован",
    "Нормально работает, ничего особенного"
]

inputs = tokenizer(texts, return_tensors='pt', padding=True, truncation=True, max_length=64)

# Прогнозирование
with torch.no_grad():
    outputs = model(**inputs)
    probabilities = F.softmax(outputs.logits, dim=1)
    predictions = torch.argmax(probabilities, dim=1)

# Вывод результатов
sentiment_labels = {0: 'негативный', 1: 'нейтральный', 2: 'позитивный'}
for text, pred, probs in zip(texts, predictions, probabilities):
    print(f"Текст: '{text}'")
    print(f"Прогноз: {sentiment_labels[pred.item()]}")
    print(f"Вероятности: негативный={probs[0]:.2f}, нейтральный={probs[1]:.2f}, позитивный={probs[2]:.2f}\n")
