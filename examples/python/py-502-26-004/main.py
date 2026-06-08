class Duck:
    def quack(self):
        return "Quack!"
    
    def walk(self):
        return "Waddle"

class RobotDuck:
    def quack(self):
        return "Beep-quack!"
    
    def walk(self):
        return "Roll"

class Human:
    def quack(self):
        return "Imitating duck"
    
    def walk(self):
        return "Bipedal walk"

def make_it_quack_and_walk(thing):
    print(f"{thing.quack()} → {thing.walk()}")

make_it_quack_and_walk(Duck())       # Quack! → Waddle
make_it_quack_and_walk(RobotDuck())   # Beep-quack! → Roll
make_it_quack_and_walk(Human())       # Imitating duck → Bipedal walk
