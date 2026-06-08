class Car {
    private String brand;
    private String model;

    // Конструктор
    public Car(String brand, String model) {
        this.brand = brand;
        this.model = model;
    }

    public void showInfo() {
        System.out.println("Марка: " + brand + ", Модель: " + model);
    }
}
// Использование
Car car1 = new Car("BMW", "X5");
car1.showInfo();
