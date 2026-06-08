import pg from "pg";
const { Client } = pg;

const client = new Client({
  host: "localhost",
  port: 5432,
  user: "app_user",
  password: "secret",
  database: "app_db",
});

await client.connect();
await client.query("CREATE TABLE IF NOT EXISTS users(id BIGSERIAL PRIMARY KEY, name TEXT NOT NULL)");
await client.query("INSERT INTO users(name) VALUES ($1)", ["Anna"]);

const res = await client.query("SELECT id, name FROM users");
for (const row of res.rows) {
  console.log(row.id, row.name);
}

await client.query("UPDATE users SET name=$1 WHERE id=$2", ["Ann", 1]);
await client.query("DELETE FROM users WHERE id=$1", [1]);
await client.end();
