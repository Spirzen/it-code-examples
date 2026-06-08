class LightBulb {
    public void turnOn() { ... }
}

class Switch {
    private LightBulb bulb = new LightBulb(); // жёсткая зависимость
}
