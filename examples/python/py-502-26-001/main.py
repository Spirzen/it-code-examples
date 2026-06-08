class Warrior:
    count = 0                     # атрибут класса (общий для всех)
    
    def __init__(self, name):
        self.name = name          # атрибут экземпляра
        Warrior.count += 1
    
    @property
    def shout(self):              # геттер без скобок
        return f"{self.name}!!!"
    
    @classmethod
    def total(cls):               # метод класса
        return cls.count
    
    @staticmethod
    def game_name():              # просто функция внутри класса
        return "Warcraft"

class Knight(Warrior):            # наследование
    def shout(self):              # переопределение
        return f"За {self.name}!"

def fight(u1, u2):                # полиморфизм через duck typing
    print(u1.shout)               # у любого юнита должен быть shout
