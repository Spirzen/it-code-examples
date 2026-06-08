use rusqlite::{params, Connection, Result};

fn main() -> Result<()> {
    let conn = Connection::open("app.db")?;
    conn.execute(
        "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT NOT NULL)",
        [],
    )?;
    conn.execute("INSERT INTO users(name) VALUES (?1)", params!["Anna"])?;

    let mut stmt = conn.prepare("SELECT id, name FROM users")?;
    let rows = stmt.query_map([], |row| {
        Ok((row.get::<_, i64>(0)?, row.get::<_, String>(1)?))
    })?;

    for row in rows {
        let (id, name) = row?;
        println!("{id} {name}");
    }
    Ok(())
}
