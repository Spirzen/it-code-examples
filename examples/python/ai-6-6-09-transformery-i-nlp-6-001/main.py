import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

name = "cointegrated/rubert-tiny2"
tokenizer = AutoTokenizer.from_pretrained(name)
model = AutoModelForSequenceClassification.from_pretrained(name)
model.eval()

text = "Продукт разочаровал, верну деньги."
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)

with torch.no_grad():
    logits = model(**inputs).logits
    pred = logits.argmax(dim=-1).item()
