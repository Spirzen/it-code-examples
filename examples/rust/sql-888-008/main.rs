use tokio_postgres::NoTls;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let (client, connection) =
        tokio_postgres::connect("host=localhost user=app_user password=secret dbname=app_db", NoTls).await?;
    tokio::spawn(async move { let _ = connection.await; });

    client.execute(
        "CREATE TABLE IF NOT EXISTS users(id BIGSERIAL PRIMARY KEY, name TEXT NOT NULL)",
        &[],
    ).await?;
    client.execute("INSERT INTO users(name) VALUES ($1)", &[&"Anna"]).await?;

    for row in client.query("SELECT id, name FROM users", &[]).await? {
        let id: i64 = row.get(0);
        let name: String = row.get(1);
        println!("{id} {name}");
    }
    Ok(())
}
