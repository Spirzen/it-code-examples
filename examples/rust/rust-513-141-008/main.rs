pub trait Locatable {
    fn position(&self) -> &Position;
}

impl Locatable for MovingObject {
    fn position(&self) -> &Position {
        &self.position
    }
}

impl Locatable for StaticObject {
    fn position(&self) -> &Position {
        &self.position
    }
}
