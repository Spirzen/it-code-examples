class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        base_sound = super().speak()
        return f"{base_sound} → Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow"

animals = [Animal(), Dog(), Cat()]
for a in animals:
    print(a.speak())
