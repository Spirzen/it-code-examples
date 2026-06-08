pub struct Unit {
    pub name: String,
    pub intel: i32,
    pub agility: i32,
    pub strength: i32,
    pub health: i32,
    pub mana: i32,
    pub level: i32,
}

impl Unit {
    fn new() -> Unit {
        Unit {
            name: String::from("Имя"),
            intel: 10,
            agility: 10,
            strength: 10,
            health: 100,
            mana: 50,
            level: 1,
        }
    }

    fn damage(&self) -> i32 {
        (self.intel + self.agility + self.strength) + (self.level * 2)
    }

    fn attack(&mut self, target: &mut Unit) {
        let dmg = self.damage();
        println!("{} атакует {} и наносит {} единиц урона.", self.name, target.name, dmg);
        target.health -= dmg;
        println!("{} теперь имеет {} здоровья.", target.name, target.health);
    }
}

fn main() {
    let mut warrior = Unit::new();
    warrior.name = String::from("Воин");
    warrior.intel = 5;
    warrior.agility = 15;
    warrior.strength = 30;

    let mut mage = Unit::new();
    mage.name = String::from("Маг");
    mage.intel = 35;
    mage.agility = 10;
    mage.strength = 5;

    warrior.attack(&mut mage);
    mage.attack(&mut warrior);
}
