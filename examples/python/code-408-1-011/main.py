# Родительский класс
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} кушает.")


# Дочерние классы
class Cat(Animal):        # Cat наследует всё от Animal
    def speak(self):
        print(f"{self.name}: Мяу!")


class Dog(Animal):
    def speak(self):
        print(f"{self.name}: Гав!")


# Создаем питомцев
cat = Cat("Мурка")
dog = Dog("Шарик")

# Метод eat общий (взят у родителя)
cat.eat()   # Мурка кушает.
dog.eat()   # Шарик кушает.

# Голоса свои
cat.speak() # Мурка: Мяу!
dog.speak() # Шарик: Гав!
