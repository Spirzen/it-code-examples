// Пример 1: Арифметические операции и проверка переполнения
fn main() {
    let a: u32 = 5;
    let b: u32 = 10;
    
    // Стандартное сложение
    let sum = a + b;
    println!("Сумма: {}", sum);
    
    // Проверка переполнения (безопасная операция)
    let max_u32 = u32::MAX;
    let overflow_result = max_u32.checked_add(1);
    
    match overflow_result {
        Some(val) => println!("Результат без переполнения: {}", val),
        None => println!("Произошло переполнение!"),
    }
}
