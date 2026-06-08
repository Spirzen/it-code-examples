
import random

# Генерация случайного целого числа от 1 до 10
dice_roll = random.randint(1, 10)
print(f"Выпавшее число на кубике: {dice_roll}")

# Выбор случайного элемента из списка
fruits = ["Яблоко", "Банан", "Вишня", "Груша"]
chosen_fruit = random.choice(fruits)
print(f"Выбранный фрукт: {chosen_fruit}")

# Перемешивание списка
cards = ["Король", "Дама", "Валет", "10", "9"]
random.shuffle(cards)
print(f"Перемешанная колода: {cards}")

# Генерация случайного числа с плавающей точкой от 0.0 до 1.0
fraction = random.random()
print(f"Дробное число: {fraction}")

# Выбор нескольких уникальных элементов
winners = random.sample(range(1, 100), 5)
print(f"Пять победителей: {winners}")
