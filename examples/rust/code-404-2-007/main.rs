// logger/src/lib.rs
pub fn info(msg: &str) {
    let now = chrono::Utc::now();
    println!("[INFO] {} {}", now.to_rfc3339(), msg);
}

// notification/src/lib.rs
use order_logger::info; // ← имя крейта, не путь!

pub fn send_email(to: &str, subject: &str, body: &str) {
    info(&format!("Sending email to {}", to));
    // ...
}

// core/src/lib.rs
use order_logger::info;

#[derive(Debug)]
pub struct Order {
    pub id: i32,
    pub items: Vec<String>,
}

pub struct OrderService;

impl OrderService {
    pub fn place_order(items: Vec<String>) -> Order {
        let order = Order { id: 1, items };
        info(&format!("Order {} placed with {} items", order.id, order.items.len()));
        order
    }
}

// app/src/main.rs
use order_core::{OrderService, Order};
use order_notification::send_email;

fn main() {
    let order = OrderService::place_order(vec!["book".into(), "pen".into()]);
    send_email("user@example.com", "Order confirmed", &format!("ID: {}", order.id));
}
