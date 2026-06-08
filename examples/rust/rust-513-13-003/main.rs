// Объявление логических переменных
let is_active: bool = true;
let is_complete: bool = false;

// Логические операции
let condition_one: bool = true;
let condition_two: bool = false;

let and_result: bool = condition_one && condition_two; // false
let or_result: bool = condition_one || condition_two;  // true
let not_result: bool = !condition_one;                 // false

// Использование в условном операторе
if is_active && !is_complete {
    println!("Задача выполняется, но еще не завершена");
}

// Сравнение возвращает bool
let x: i32 = 10;
let y: i32 = 20;
let is_less: bool = x < y; // true
let is_equal: bool = x == y; // false

println!("x меньше y: {}", is_less);
