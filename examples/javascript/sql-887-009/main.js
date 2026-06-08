import Database from "better-sqlite3";

const db = new Database("app.db");
db.exec("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT NOT NULL)");

const ins = db.prepare("INSERT INTO users(name) VALUES (?)");
ins.run("Anna");

const rows = db.prepare("SELECT id, name FROM users").all();
for (const row of rows) {
  console.log(row.id, row.name);
}

db.prepare("UPDATE users SET name = ? WHERE id = ?").run("Ann", 1);
db.prepare("DELETE FROM users WHERE id = ?").run(1);
db.close();
