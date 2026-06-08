// Объявление кортежа с различными типами данных
let mixed_tuple = (500, 6.4, 'a');

// Доступ к элементам по индексу
let first_element = mixed_tuple.0; // Значение 500
let second_element = mixed_tuple.1; // Значение 6.4
let third_element = mixed_tuple.2; // Значение 'a'

println!("Первый элемент: {}", first_element);
println!("Второй элемент: {}", second_element);
println!("Третий элемент: {}", third_element);

// Деструктуризация кортежа
let (number, float_val, symbol) = mixed_tuple;

println!("Разложенное число: {}", number);
println!("Разложенная дробь: {}", float_val);
println!("Разложенный символ: {}", symbol);

// Использование в качестве возвращаемого значения функции
fn get_user_data() -> (String, i32, bool) {
    ("Alice".to_string(), 30, true)
}

let (name, age, is_active) = get_user_data();
println!("Пользователь: {}, Возраст: {}, Активен: {}", name, age, is_active);

// Пустой кортеж (единственный элемент)
let empty_tuple = ();
