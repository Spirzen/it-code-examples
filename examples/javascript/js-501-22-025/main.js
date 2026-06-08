class Shape {
    constructor(color = 'black') {
        this.color = color;
    }
    
    draw() {
        console.log(`Рисую фигуру цветом ${this.color}`);
    }
}

class Circle extends Shape {
    constructor(radius, color) {
        super(color);
        this.radius = radius;
    }
    
    getArea() {
        return Math.PI * this.radius * this.radius;
    }
    
    draw() {
        console.log(`Рисую круг радиусом ${this.radius}`);
        super.draw();
    }
}

class Rectangle extends Shape {
    constructor(width, height, color) {
        super(color);
        this.width = width;
        this.height = height;
    }
    
    getArea() {
        return this.width * this.height;
    }
    
    draw() {
        console.log(`Рисую прямоугольник ${this.width}x${this.height}`);
        super.draw();
    }
}

const circle = new Circle(5, 'red');
const rect = new Rectangle(10, 20, 'blue');

circle.draw();
console.log(`Площадь круга: ${circle.getArea()}`);

rect.draw();
console.log(`Площадь прямоугольника: ${rect.getArea()}`);
