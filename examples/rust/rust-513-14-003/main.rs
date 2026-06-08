fn divide(a: i32, b: i32) -> Option<i32> {
    if b == 0 {
        None
    } else {
        Some(a / b)
    }
}

fn main() {
    match divide(10, 2) {
        Some(value) => println!("Результат: {}", value),
        None => println!("Деление на ноль"),
    }
}
