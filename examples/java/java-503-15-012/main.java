// Простая запись с двумя компонентами
record Point(int x, int y) {}

// Использование записи
Point p1 = new Point(10, 20);
int x = p1.x();                  // 10 — геттер с именем компонента
int y = p1.y();                  // 20
Point p2 = new Point(10, 20);
System.out.println(p1.equals(p2)); // true — сравнение по значениям компонентов
System.out.println(p1);          // Point[x=10, y=20] — сгенерированный toString()

// Запись с дополнительным конструктором
record Person(String name, int age) {
    // Компактный конструктор для валидации
    Person {
        if (age < 0 || age > 150) {
            throw new IllegalArgumentException("Некорректный возраст");
        }
    }
}

Person valid = new Person("Анна", 30); // успешно создаётся
// Person invalid = new Person("Борис", -5); // исключение

// Запись с несколькими компонентами разных типов
record Product(String id, String name, double price, boolean inStock) {}

Product laptop = new Product("P123", "Ноутбук", 59999.99, true);
String id = laptop.id();         // "P123"
double price = laptop.price();   // 59999.99

// Вложенные записи
record Address(String street, String city, String postalCode) {}
record Customer(String name, Address address, String email) {}

Address addr = new Address("Ленина, 10", "Москва", "123456");
Customer customer = new Customer("Иван Петров", addr, "ivan@example.com");
String city = customer.address().city(); // "Москва"

// Запись как возвращаемый тип метода
record CalculationResult(double sum, double average, int count) {}

CalculationResult calculate(int[] values) {
    double sum = 0;
    for (int v : values) sum += v;
    return new CalculationResult(sum, sum / values.length, values.length);
}

CalculationResult result = calculate(new int[]{10, 20, 30});
System.out.println(result.average()); // 20.0
