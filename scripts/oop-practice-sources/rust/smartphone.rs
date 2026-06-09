struct Smartphone {
    model: String,
    battery: i32,
}

impl Smartphone {
    fn new(model: &str) -> Self {
        Self {
            model: model.to_string(),
            battery: 20,
        }
    }

    fn call(&mut self) {
        self.battery = (self.battery - 5).max(0);
        println!("Звонок с {}... Заряд: {}%", self.model, self.battery);
    }

    fn charge(&mut self) {
        self.battery = (self.battery + 30).min(100);
        println!("Зарядка {}... Заряд: {}%", self.model, self.battery);
    }

    fn show_status(&self) {
        println!("Смартфон {}: заряд {}%", self.model, self.battery);
    }
}

fn main() {
    let mut phone = Smartphone::new("Pixel");
    phone.show_status();
    phone.call();
    phone.charge();
    phone.show_status();
}
