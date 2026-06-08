
import json

from pymemcache.client.base import Client

client = Client(("127.0.0.1", 11211))

def get_user_profile(user_id: int) -> dict | None:
    key = f"user:profile:{user_id}"
    raw = client.get(key)
    if raw is not None:
        return json.loads(raw)

    row = fetch_user_from_db(user_id)  # ваша функция доступа к PostgreSQL и т.д.
    if row is not None:
        client.set(key, json.dumps(row), expire=3600)
    return row

def invalidate_user_profile(user_id: int) -> None:
    client.delete(f"user:profile:{user_id}")
