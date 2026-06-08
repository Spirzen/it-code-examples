from abc import ABC, abstractmethod

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def bounding_box(self):
        pass

class Circle(Drawable):
    def draw(self):
        print("Drawing circle")

    def bounding_box(self):
        return (0, 0, 10, 10)

# Drawable()  # Ошибка — нельзя создать экземпляр абстрактного класса
