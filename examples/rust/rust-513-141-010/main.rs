pub trait Drawable {
    fn draw(&self);
}

pub trait Serializable {
    fn serialize(&self) -> String;
}

pub struct Widget {
    id: u32,
    name: String,
}

impl Drawable for Widget {
    fn draw(&self) {
        println!("Drawing widget {}", self.name);
    }
}

impl Serializable for Widget {
    fn serialize(&self) -> String {
        format!("{{\"id\":{},\"name\":\"{}\"}}", self.id, self.name)
    }
}
