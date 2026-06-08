struct Cat {
    name: String,
    age: u8,
}

impl Cat {
    fn meow(&self) {
        println!("{} ({}) говорит: мяу!", self.name, self.age);
    }
}

fn main() {
    let barsik = Cat {
        name: String::from("Барсик"),
        age: 3,
    };
    barsik.meow();
}
