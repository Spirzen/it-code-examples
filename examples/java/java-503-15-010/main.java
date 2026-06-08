// Явная упаковка через конструкторы (устаревший подход)
Integer boxedInt = new Integer(42);      // устаревшее, предпочтительно valueOf()
Double boxedDouble = new Double(3.14);   // устаревшее

// Явная упаковка через valueOf (рекомендуется)
Integer a = Integer.valueOf(100);        // из кэша для значений -128..127
Integer b = Integer.valueOf(100);        // тот же объект из кэша
Integer c = Integer.valueOf(200);        // новый объект (вне кэша)
Integer d = Integer.valueOf(200);        // новый объект

System.out.println(a == b); // true — кэшированные объекты
System.out.println(c == d); // false — разные объекты

// Автоматическая упаковка (с Java 5)
Integer autoBoxed = 42;                  // компилятор вставляет Integer.valueOf(42)
Double autoBoxedDouble = 3.14;           // Double.valueOf(3.14)
Boolean autoBoxedBoolean = true;         // Boolean.valueOf(true)

// Автоматическая распаковка
int unboxedInt = autoBoxed;              // компилятор вставляет autoBoxed.intValue()
double unboxedDouble = autoBoxedDouble;  // autoBoxedDouble.doubleValue()

// Опасность распаковки null
Integer nullable = null;
// int dangerous = nullable; // NullPointerException при распаковке!

// Безопасная распаковка с проверкой
int safeValue = (nullable != null) ? nullable : 0;

// Использование в коллекциях
List<Integer> numbers = new ArrayList<>();
numbers.add(10);        // автоматическая упаковка
numbers.add(20);
int first = numbers.get(0); // автоматическая распаковка

// Сравнение через equals для корректности
Integer x = 200;
Integer y = 200;
System.out.println(x.equals(y)); // true — корректное сравнение значений
System.out.println(x == y);      // false — разные объекты
