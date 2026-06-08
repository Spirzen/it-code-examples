// Создание строк разными способами
String literal = "Привет, мир!";          // строковый литерал (интернируется)
String constructor = new String("Привет"); // новый объект вне пула строк
String fromCharArray = new String(new char[]{'J', 'a', 'v', 'a'}); // из массива символов
String empty = "";                        // пустая строка
String nullString = null;                 // отсутствие строки

// Неизменяемость строк
String original = "hello";
String upper = original.toUpperCase();    // "HELLO" — новая строка
String replaced = original.replace('l', 'L'); // "heLLo" — новая строка
// original остаётся "hello"

// Конкатенация
String firstName = "Иван";
String lastName = "Иванов";
String fullName = firstName + " " + lastName; // "Иван Иванов"
String withAge = "Возраст: " + 25;           // "Возраст: 25" — число преобразуется в строку

// Форматирование
String formatted = String.format("Пользователь %s, возраст %d", "Анна", 30);
// "Пользователь Анна, возраст 30"

// Работа с пулом строк
String s1 = "pool";               // литерал — помещается в пул
String s2 = "pool";               // тот же объект из пула
String s3 = new String("pool");   // новый объект вне пула
String s4 = s3.intern();          // явное интернирование — возвращает объект из пула

System.out.println(s1 == s2); // true — один объект
System.out.println(s1 == s3); // false — разные объекты
System.out.println(s1 == s4); // true — после интернирования

// Полезные методы
String text = "  Java Programming  ";
String trimmed = text.trim();           // "Java Programming" — удаление пробелов по краям
String lower = text.toLowerCase();      // "  java programming  "
String upper = text.toUpperCase();      // "  JAVA PROGRAMMING  "
boolean contains = text.contains("Java"); // true
int index = text.indexOf('P');          // 7 — позиция первого 'P'
String substring = text.substring(2, 6); // "Java"
