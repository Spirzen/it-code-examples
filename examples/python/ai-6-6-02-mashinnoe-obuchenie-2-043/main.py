from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset

import numpy as np

from sklearn.metrics import accuracy_score, f1_score

# Загрузка предобученной модели и токенизатора
model_name = "DeepPavlov/rubert-base-cased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(
    model_name,
    num_labels=3,  # три класса тональности
    ignore_mismatched_sizes=True  # разрешить изменение размера выходного слоя
)

# Подготовка данных (пример с синтетическими данными)
texts = [
    "Отличный сервис и быстрая доставка",
    "Ужасное качество, больше не куплю",
    "Нормально, но можно лучше",
    "Восхитительно! Рекомендую всем",
    "Полное разочарование, деньги на ветер"
]
labels = [2, 0, 1, 2, 0]  # 0 - негатив, 1 - нейтральный, 2 - позитив

# Токенизация
encodings = tokenizer(texts, truncation=True, padding=True, max_length=128)

# Создание датасета
class SentimentDataset:
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels
    
    def __getitem__(self, idx):
        item = {key: val[idx] for key, val in self.encodings.items()}
        item['labels'] = self.labels[idx]
        return item
    
    def __len__(self):
        return len(self.labels)

dataset = SentimentDataset(encodings, labels)

# Функция вычисления метрик
def compute_metrics(pred):
    labels = pred.label_ids
    preds = pred.predictions.argmax(-1)
    acc = accuracy_score(labels, preds)
    f1 = f1_score(labels, preds, average='weighted')
    return {'accuracy': acc, 'f1': f1}

# Настройка обучения
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=2,
    learning_rate=2e-5,
    weight_decay=0.01,
    logging_steps=10,
    save_strategy='no'
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    compute_metrics=compute_metrics
)

# Обучение модели
trainer.train()

# Прогнозирование на новых данных
test_texts = ["Качество превзошло ожидания", "Не советую покупать"]
test_encodings = tokenizer(test_texts, truncation=True, padding=True, max_length=128, return_tensors='pt')

with torch.no_grad():
    outputs = model(**test_encodings)
    predictions = torch.argmax(outputs.logits, dim=1)

sentiment_map = {0: 'негативный', 1: 'нейтральный', 2: 'позитивный'}
for text, pred in zip(test_texts, predictions):
    print(f"'{text}' -> {sentiment_map[pred.item()]}")
