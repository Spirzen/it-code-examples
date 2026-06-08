interface Switchable {
    void turnOn();
    void turnOff();
}

class LightBulb implements Switchable { ... }
class Fan implements Switchable { ... }

class Switch {
    private Switchable device; // зависит от абстракции
    public Switch(Switchable device) {
        this.device = device;
    }
}
