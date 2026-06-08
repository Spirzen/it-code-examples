use mongodb::{Client, options::ClientOptions};
use serde::{Deserialize, Serialize};

#[derive(Serialize, Deserialize)]
struct User {
    name: String,
    email: String,
}

#[tokio::main]
async fn main() -> mongodb::error::Result<()> {
    let client_options = ClientOptions::parse("mongodb://localhost:27017").await?;
    let client = Client::with_options(client_options)?;

    let db = client.database("mydb");
    let collection = db.collection::<User>("users");

    let user = User {
        name: "Alice".to_string(),
        email: "alice@example.com".to_string(),
    };

    collection.insert_one(user, None).await?;

    Ok(())
}
