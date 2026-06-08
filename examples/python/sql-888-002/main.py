import psycopg

conn = psycopg.connect("host=localhost dbname=app_db user=app_user password=secret")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users(
    id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL
)
""")
cur.execute("INSERT INTO users(name) VALUES (%s)", ("Anna",))
conn.commit()

cur.execute("SELECT id, name FROM users")
for row in cur.fetchall():
    print(row[0], row[1])

cur.execute("UPDATE users SET name=%s WHERE id=%s", ("Ann", 1))
cur.execute("DELETE FROM users WHERE id=%s", (1,))
conn.commit()
conn.close()
