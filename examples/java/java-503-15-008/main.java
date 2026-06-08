// Примитивы сравниваются по значению оператором ==
int a = 100;
int b = 100;
System.out.println(a == b); // true — значения равны

// Ссылочные типы: сравнение ссылок оператором ==
String s1 = "hello";
String s2 = "hello";
System.out.println(s1 == s2); // true — один объект из пула строк

String s3 = new String("hello");
String s4 = new String("hello");
System.out.println(s3 == s4); // false — разные объекты
System.out.println(s3.equals(s4)); // true — содержимое одинаково

// Автоматическая упаковка и кэширование
Integer boxed1 = 100;
Integer boxed2 = 100;
System.out.println(boxed1 == boxed2); // true — кэшированные объекты

Integer boxed3 = 200;
Integer boxed4 = 200;
System.out.println(boxed3 == boxed4); // false — разные объекты вне кэша
System.out.println(boxed3.equals(boxed4)); // true — значения равны

// Сравнение примитива и обёртки
int primitive = 42;
Integer wrapper = 42;
System.out.println(primitive == wrapper); // true — wrapper распаковывается автоматически
