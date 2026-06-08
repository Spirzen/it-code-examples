// Пример 4: Цикл while с проверкой условия перед выполнением
fn countdown(start: i32) {
    let mut counter = start;
    
    while counter >= 0 {
        println!("Таймер: {}", counter);
        counter -= 1;
    }
    println!("Поехали!");
}

fn main() {
    countdown(3);
}
