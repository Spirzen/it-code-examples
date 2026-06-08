// Числа с плавающей запятой
let single_precision: f32 = 3.14_f32;
let double_precision: f64 = 2.718281828459045;

// Явное указание типа для литерала
let pi_approx: f32 = 3.14;

// Арифметические операции
let sum: f64 = 10.5 + 5.25;
let product: f32 = 2.5 * 4.0;
let division: f64 = 10.0 / 3.0;

// Проверка специальных значений
let infinity: f64 = f64::INFINITY;
let not_a_number: f32 = f32::NAN;
let zero: f64 = 0.0;

println!("Сумма: {}", sum);
println!("Произведение: {}", product);
println!("Деление: {}", division);
