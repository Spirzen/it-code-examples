use mysql::*;
use mysql::prelude::*;

fn main() -> Result<()> {
    let pool = Pool::new("mysql://app_user:secret@localhost:3306/app_db")?;
    let mut conn = pool.get_conn()?;

    conn.query_drop("CREATE TABLE IF NOT EXISTS users(id BIGINT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255) NOT NULL) ENGINE=InnoDB")?;
    conn.exec_drop("INSERT INTO users(name) VALUES (?)", ("Anna",))?;

    let rows: Vec<(u64, String)> = conn.query("SELECT id, name FROM users")?;
    for (id, name) in rows {
        println!("{id} {name}");
    }
    Ok(())
}
