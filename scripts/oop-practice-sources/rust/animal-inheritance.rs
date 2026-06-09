struct Animal {
    name: String,
}

impl Animal {
    fn eat(&self) {
        println!("{} ест", self.name);
    }
}

struct Cat {
    animal: Animal,
}

impl Cat {
    fn new(name: &str) -> Self {
        Self {
            animal: Animal {
                name: name.to_string(),
            },
        }
    }

    fn eat(&self) {
        self.animal.eat();
    }

    fn speak(&self) {
        println!("Мяу!");
    }
}

struct Dog {
    animal: Animal,
}

impl Dog {
    fn new(name: &str) -> Self {
        Self {
            animal: Animal {
                name: name.to_string(),
            },
        }
    }

    fn eat(&self) {
        self.animal.eat();
    }

    fn speak(&self) {
        println!("Гав!");
    }
}

fn main() {
    let cat = Cat::new("Мурка");
    let dog = Dog::new("Шарик");
    cat.eat();
    cat.speak();
    dog.eat();
    dog.speak();
}
