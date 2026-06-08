import mysql.connector

conn = mysql.connector.connect(
    host="localhost", port=3306, user="app_user", password="secret", database="app_db"
)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users(
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL
) ENGINE=InnoDB
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
