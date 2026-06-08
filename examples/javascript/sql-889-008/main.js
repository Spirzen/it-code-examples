import mysql from "mysql2/promise";

const conn = await mysql.createConnection({
  host: "localhost",
  port: 3306,
  user: "app_user",
  password: "secret",
  database: "app_db",
});

await conn.execute(
  "CREATE TABLE IF NOT EXISTS users(id BIGINT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255) NOT NULL) ENGINE=InnoDB"
);
await conn.execute("INSERT INTO users(name) VALUES (?)", ["Anna"]);

const [rows] = await conn.execute("SELECT id, name FROM users");
for (const row of rows) {
  console.log(row.id, row.name);
}

await conn.execute("UPDATE users SET name=? WHERE id=?", ["Ann", 1]);
await conn.execute("DELETE FROM users WHERE id=?", [1]);
await conn.end();
