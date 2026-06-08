
import math

# Использование констант
print(f"Число Пи: {math.pi}")
print(f"Число Эйлера: {math.e}")

# Тригонометрия
angle_in_degrees = 45
angle_in_radians = math.radians(angle_in_degrees)
sine_value = math.sin(angle_in_radians)
print(f"Синус угла {angle_in_degrees} градусов равен: {sine_value}")

# Возведение в степень и корни
base = 2
exponent = 10
power_result = math.pow(base, exponent)
print(f"{base} в степени {exponent} равно: {power_result}")

square_root = math.sqrt(144)
print(f"Квадратный корень из 144 равен: {square_root}")

# Округление
number = 3.14159265
rounded_number = round(number, 2)
print(f"Округленное значение: {rounded_number}")
