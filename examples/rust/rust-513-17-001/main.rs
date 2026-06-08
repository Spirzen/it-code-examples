use tokio::time::{sleep, Duration};

async fn fetch_label(name: &str, ms: u64) -> String {
    sleep(Duration::from_millis(ms)).await;
    format!("{name}: ready")
}

#[tokio::main]
async fn main() {
    let (a, b) = tokio::join!(
        fetch_label("users", 200),
        fetch_label("orders", 300),
    );
    println!("{a}, {b}");
}
