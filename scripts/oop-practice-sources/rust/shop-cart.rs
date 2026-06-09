#[derive(Clone)]
struct Product {
    name: String,
    price: i32,
}

struct Cart {
    items: Vec<Product>,
}

impl Cart {
    fn new() -> Self {
        Self { items: Vec::new() }
    }

    fn add(&mut self, product: Product) {
        println!(
            "В корзину добавлено: {} ({} ₽)",
            product.name, product.price
        );
        self.items.push(product);
    }

    fn total(&self) -> i32 {
        self.items.iter().map(|p| p.price).sum()
    }
}

struct Order {
    items: Vec<Product>,
    total: i32,
}

impl Order {
    fn new(cart: &Cart) -> Self {
        Self {
            items: cart.items.clone(),
            total: cart.total(),
        }
    }

    fn checkout(&self) {
        println!("Оформление заказа...");
        for item in &self.items {
            println!("  — {}: {} ₽", item.name, item.price);
        }
        println!("Итого: {} ₽", self.total);
        println!("Заказ оформлен!");
    }
}

fn main() {
    let mut cart = Cart::new();
    cart.add(Product {
        name: "Книга".to_string(),
        price: 500,
    });
    cart.add(Product {
        name: "Ручка".to_string(),
        price: 50,
    });
    let order = Order::new(&cart);
    order.checkout();
}
