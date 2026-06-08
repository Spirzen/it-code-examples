import requests

# --- GET ---
r = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1",
    timeout=10,
)
r.raise_for_status()
data = r.json()
print("Заголовок:", data["title"])

# --- POST JSON ---
r = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json={"title": "hello", "body": "text", "userId": 1},
    timeout=10,
)
r.raise_for_status()
created = r.json()
print("Новый id:", created["id"])
