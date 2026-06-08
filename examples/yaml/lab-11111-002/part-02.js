const http = require('http');
const { Client } = require('pg');

const client = new Client({
  host: process.env.DB_HOST,
  port: process.env.DB_PORT,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
});

client.connect()
  .then(() => {
    http.createServer((_req, res) => {
      res.end('API + Postgres OK');
    }).listen(3000);
  })
  .catch((err) => {
    console.error('DB error:', err.message);
    process.exit(1);
  });
