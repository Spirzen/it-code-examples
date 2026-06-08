class Vehicle {
    protected String brand;

    // Явный конструктор
    public Vehicle(String brand) {
        this.brand = brand;
        System.out.println("Vehicle constructor called");
    }
}

class Car extends Vehicle {
    private int doors;

    // Конструктор Car обязан вызвать конструктор Vehicle
    public Car(String brand, int doors) {
        super(brand); // обязательный вызов суперконструктора
        this.doors = doors;
        System.out.println("Car constructor called");
    }
}

// Использование
Car myCar = new Car("Toyota", 4);
// Вывод:
// Vehicle constructor called
// Car constructor called
