public class Person {
    private String name;
    private int age;

    // Обычный конструктор
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Конструктор копирования
    public Person(Person other) {
        this.name = other.name;
        this.age = other.age;
    }
}
