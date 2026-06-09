class Smartphone {
    private String model;
    private int battery;

    Smartphone(String model) {
        this.model = model;
        this.battery = 20;
    }

    void call() {
        battery = Math.max(0, battery - 5);
        System.out.println("Звонок с " + model + "... Заряд: " + battery + "%");
    }

    void charge() {
        battery = Math.min(100, battery + 30);
        System.out.println("Зарядка " + model + "... Заряд: " + battery + "%");
    }

    void showStatus() {
        System.out.println("Смартфон " + model + ": заряд " + battery + "%");
    }
}

public class Main {
    public static void main(String[] args) {
        Smartphone phone = new Smartphone("Pixel");
        phone.showStatus();
        phone.call();
        phone.charge();
        phone.showStatus();
    }
}
