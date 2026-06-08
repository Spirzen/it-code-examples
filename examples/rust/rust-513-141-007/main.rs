#[derive(Debug, Clone)]
pub struct Position {
    pub x: f64,
    pub y: f64,
}

pub struct MovingObject {
    pub position: Position,
    pub velocity: f64,
}

pub struct StaticObject {
    pub position: Position,
    pub label: String,
}
