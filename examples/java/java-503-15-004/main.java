// Буквенные символы
char letter = 'A';               // латинская буква
char cyrillic = 'Я';             // кириллическая буква
char digit = '7';                // цифра как символ

// Управляющие символы
char newline = '\n';             // символ новой строки
char tab = '\t';                 // символ табуляции
char backspace = '\b';           // символ возврата на шаг

// Unicode escape-последовательности
char euro = '\u20AC';            // символ евро €
char copyright = '\u00A9';       // символ авторского права ©
char heart = '\u2665';           // символ сердца ♥

// Арифметические операции с char (преобразование в число)
char nextLetter = (char)('A' + 1); // 'B'
int charCode = 'A';              // 65 — код символа в UTF-16
char fromCode = (char)66;        // 'B'

// Массив символов
char[] word = {'H', 'e', 'l', 'l', 'o'};
String fromCharArray = new String(word); // "Hello"
