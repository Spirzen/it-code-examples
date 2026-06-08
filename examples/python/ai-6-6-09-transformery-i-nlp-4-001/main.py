from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer
from datasets import load_dataset

model_name = "cointegrated/rubert-tiny2"
num_labels = 2

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=num_labels)

ds = load_dataset("blinoff/rusentiment", split="train[:2000]")
ds = ds.rename_column("text", "sentence")

def tokenize(batch):
    return tokenizer(batch["sentence"], truncation=True, padding="max_length", max_length=128)

ds = ds.map(tokenize, batched=True)
ds = ds.rename_column("label", "labels")
ds.set_format("torch")

args = TrainingArguments(
    output_dir="./out",
    per_device_train_batch_size=16,
    num_train_epochs=3,
    learning_rate=2e-5,
    evaluation_strategy="no",
)

trainer = Trainer(model=model, args=args, train_dataset=ds)
trainer.train()
