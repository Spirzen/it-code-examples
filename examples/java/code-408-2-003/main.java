interface Flyable {
    void fly();  // абстрактный метод
}

class Bird implements Flyable {
    public void fly() {
        System.out.println("Лечу как птица!");
    }
}
