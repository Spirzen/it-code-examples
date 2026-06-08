// Объявление символов разных категорий
let ascii_letter: char = 'A';
let cyrillic_letter: char = 'Я';
let emoji: char = '🚀';
let math_symbol: char = '∑';
let digit: char = '5';

// Проверка длины и свойств
let text = "Привет";
let first_char = text.chars().next(); // Первый символ строки

// Работа с эмодзи и сложными символами
let heart: char = '❤'; // Один Unicode scalar (без вариационного селектора)
let kanji: char = '日'; // Иероглиф "день"

// Сравнение символов
let is_uppercase = 'A' > 'a'; // false
let is_digit = '5' >= '0';     // true

// Вывод символов
println!("Буква: {}", ascii_letter);
println!("Эмодзи: {}", emoji);
println!("Сердце: {}", heart);
println!("Иероглиф: {}", kanji);

// Преобразование символа в его код
let code_point = 'A' as u32; // 65
