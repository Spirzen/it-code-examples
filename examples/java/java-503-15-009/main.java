// Расширение (widening) — неявное, безопасное
byte b = 10;
int i = b;                       // byte → int
long l = i;                      // int → long
double d = l;                    // long → double

char c = 'A';
int charCode = c;                // char → int (65)

// Сужение (narrowing) — явное, потенциально опасное
double pi = 3.14159;
int truncated = (int) pi;        // 3 — дробная часть отброшена

long big = 3_000_000_000L;
int overflow = (int) big;        // -1294967296 — переполнение

int negative = -1;
char unsignedChar = (char) negative; // '\uffff' (65535)

// Расширение при арифметических операциях
byte a = 10;
byte b2 = 20;
// byte sum = a + b2; // ошибка компиляции — результат имеет тип int
byte sum = (byte)(a + b2);       // 30 — требуется явное приведение

// Приведение ссылочных типов в иерархии наследования
Object obj = "Строка";
String str = (String) obj;       // безопасное приведение

Object number = 42;
// String text = (String) number; // ClassCastException при выполнении

// Проверка типа перед приведением
if (obj instanceof String) {
    String s = (String) obj;
    System.out.println(s.length());
}

// Современный синтаксис с паттерн-матчингом (Java 16+)
if (obj instanceof String s) {
    System.out.println(s.length()); // переменная s доступна здесь
}
