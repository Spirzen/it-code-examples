// Пример 3: Бесконечный цикл loop с возвратом значения
fn find_first_even_number(limit: i32) -> Option<i32> {
    let mut num = 0;
    
    loop {
        if num > limit {
            return None; // Прерывание цикла без возврата значения из тела
        }
        
        if num % 2 == 0 {
            break Some(num); // Возврат значения при выходе из цикла
        }
        
        num += 1;
    }
}

fn main() {
    if let Some(number) = find_first_even_number(10) {
        println!("Первое чётное число до {}: {}", 10, number);
    } else {
        println!("Чётные числа не найдены");
    }
}
