
import sqlite3

conn = sqlite3.connect("example.db")
conn.execute("PRAGMA foreign_keys = ON")
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT NOT NULL
    )
""")
cur.execute("INSERT INTO users (username, email) VALUES (?, ?)", ("bob", "bob@example.com"))
conn.commit()
