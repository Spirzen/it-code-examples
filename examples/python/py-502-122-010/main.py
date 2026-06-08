
import json

user = {
    "name": "Алексей",
    "age": 30,
    "skills": ["Python", "SQL", "Docker"]
}

json_text = json.dumps(user, ensure_ascii=False, indent=2)
print("JSON-строка:\n", json_text)

parsed_user = json.loads(json_text)
print("Имя после обратного преобразования:", parsed_user["name"])
