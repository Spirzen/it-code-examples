# 1. Создаем чертеж (класс) для любой фигуры
class Figure:
    def __init__(self, name, color):
        self.name = name    # Характеристика (поле)
        self.color = color

    def describe(self):     # Действие (метод)
        print(f"Я {self.color} {self.name}")


# 2. Создаем конкретные фигуры (объекты)
circle = Figure("Круг", "Красный")
square = Figure("Квадрат", "Синий")

# 3. Используем их
circle.describe()   # Вывод: Я Красный Круг
square.describe()   # Вывод: Я Синий Квадрат
