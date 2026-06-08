use tokio_postgres::{NoTls, Client};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let (client, connection) = tokio_postgres::connect(
        "host=localhost user=me dbname=mydb",
        NoTls,
    ).await?;

    tokio::spawn(async move {
        if let Err(e) = connection.await {
            eprintln!("connection error: {}", e);
        }
    });

    let rows = client
        .query("SELECT id, name FROM users WHERE age > $1", &[&18])
        .await?;

    for row in rows {
        let id: i32 = row.get(0);
        let name: &str = row.get(1);
        println!("{}: {}", id, name);
    }

    Ok(())
}
