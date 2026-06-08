public class Person {
    private final String name;
    private final LocalDate birthDate;

    public Person(String name, LocalDate birthDate) {
        this.name = name;
        this.birthDate = birthDate;
    }

    // Копирующий конструктор
    public Person(Person original) {
        this(original.name, original.birthDate);
    }

    // Фабричный метод — более гибкий
    public static Person copyOf(Person original) {
        return new Person(original.name, original.birthDate);
    }
}
