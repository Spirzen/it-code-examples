import sqlite3

conn = sqlite3.connect("bot.db")
conn.execute(
    "CREATE TABLE IF NOT EXISTS users (tg_id INTEGER PRIMARY KEY, name TEXT, score INTEGER DEFAULT 0)"
)

def upsert_user(tg_id: int, name: str) -> None:
    conn.execute(
        "INSERT INTO users (tg_id, name) VALUES (?, ?) "
        "ON CONFLICT(tg_id) DO UPDATE SET name = excluded.name",
        (tg_id, name),
    )
    conn.commit()
