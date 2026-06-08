// Интерфейс двигателя
interface Engine {
    void start();
    void stop();
}

// Конкретная реализация: бензиновый двигатель
class GasEngine implements Engine {
    @Override
    public void start() {
        System.out.println("Запуск бензинового двигателя");
    }

    @Override
    public void stop() {
        System.out.println("Остановка бензинового двигателя");
    }
}

// Конкретная реализация: электродвигатель
class ElectricEngine implements Engine {
    @Override
    public void start() {
        System.out.println("Запуск электродвигателя");
    }

    @Override
    public void stop() {
        System.out.println("Остановка электродвигателя");
    }
}

// Автомобиль "имеет" двигатель — композиция
class Car {
    private Engine engine;

    // Двигатель передаётся при создании — гибкость!
    public Car(Engine engine) {
        this.engine = engine;
    }

    public void start() {
        engine.start();
    }

    public void stop() {
        engine.stop();
    }

    // Возможность заменить двигатель во время выполнения
    public void setEngine(Engine engine) {
        this.engine = engine;
    }
}
