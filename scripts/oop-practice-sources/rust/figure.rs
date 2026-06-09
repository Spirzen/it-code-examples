struct Figure {
    name: String,
    color: String,
}

impl Figure {
    fn describe(&self) {
        println!("Фигура «{}», цвет: {}", self.name, self.color);
    }
}

struct Circle {
    figure: Figure,
}

impl Circle {
    fn new(color: &str) -> Self {
        Self {
            figure: Figure {
                name: "Круг".to_string(),
                color: color.to_string(),
            },
        }
    }

    fn describe(&self) {
        self.figure.describe();
    }
}

struct Square {
    figure: Figure,
}

impl Square {
    fn new(color: &str) -> Self {
        Self {
            figure: Figure {
                name: "Квадрат".to_string(),
                color: color.to_string(),
            },
        }
    }

    fn describe(&self) {
        self.figure.describe();
    }
}

fn main() {
    let circle = Circle::new("красный");
    let square = Square::new("синий");
    circle.describe();
    square.describe();
}
