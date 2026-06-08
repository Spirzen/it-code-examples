// Плохой пример нарушения LSP: "квадрат" с отдельными width/height
class Rectangle {
  constructor(public width: number, public height: number) {}
  setWidth(w: number) { this.width = w; }
  setHeight(h: number) { this.height = h; }
  area() { return this.width * this.height; }
}

// Подтип не должен ломать код, который ждёт произвольный прямоугольник
function doubleWidth(r: Rectangle) {
  const before = r.area();
  r.setWidth(r.width * 2);
  // Для настоящего Rectangle площадь выросла в 2 раза — для "квадрата-наследника" может нет
}
