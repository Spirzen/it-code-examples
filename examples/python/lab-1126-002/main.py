import json

data = {
    "title": "Мой проект",
    "version": 1,
    "tags": ["python", "files"],
}

with open("config.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with open("config.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded["title"])
