
import json

data = {
    "users": [
        {"id": 1, "name": "Alice", "active": True},
        {"id": 2, "name": "Bob", "active": False}
    ],
    "total": 2
}

# Сериализация в строку
json_str = json.dumps(data, indent=2)
print(json_str)

# Сохранение в файл
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Чтение из файла
with open('data.json', 'r', encoding='utf-8') as f:
    loaded_data = json.load(f)
