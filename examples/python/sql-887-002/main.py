import sqlite3

conn = sqlite3.connect("app.db")
conn.row_factory = sqlite3.Row
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
)
""")

cur.execute("INSERT INTO users(name) VALUES (?)", ("Anna",))
conn.commit()

cur.execute("SELECT id, name FROM users")
rows = cur.fetchall()
for row in rows:
    print(row["id"], row["name"])

cur.execute("UPDATE users SET name=? WHERE id=?", ("Ann", 1))
cur.execute("DELETE FROM users WHERE id=?", (1,))
conn.commit()
conn.close()
