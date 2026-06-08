interface Drawable {
    void draw();
}

class Circle implements Drawable {
    public void draw() { System.out.println("Рисуем круг"); }
}

class Chart implements Drawable {
    public void draw() { System.out.println("Рисуем диаграмму"); }
}

List<Drawable> items = Arrays.asList(new Circle(), new Chart());
for (Drawable d : items) {
    d.draw(); // полиморфный вызов
}
