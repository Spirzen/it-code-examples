use tokio::sync::mpsc;

#[tokio::main]
async fn main() {
    let (tx, mut rx) = mpsc::channel(16);

    tokio::spawn(async move {
        tx.send("ping".to_string()).await.unwrap();
    });

    if let Some(msg) = rx.recv().await {
        println!("received: {msg}");
    }
}
