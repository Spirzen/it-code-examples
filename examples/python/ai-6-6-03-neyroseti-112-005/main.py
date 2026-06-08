from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments
from datasets import load_dataset

# Загрузка предобученной модели и токенизатора
model_name = "ai-forever/mGPT"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Подготовка предметного набора данных
dataset = load_dataset("text", data_files={"train": "legal_documents.txt"})
dataset = dataset.map(lambda Примеры: tokenizer(Примеры["text"], truncation=True, padding="max_length", max_length=512), batched=True)

# Настройка параметров обучения
training_args = TrainingArguments(
    output_dir="./legal_model",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    save_steps=500,
    save_total_limit=2,
    learning_rate=2e-5,
)

# Обучение
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
)
trainer.train()
