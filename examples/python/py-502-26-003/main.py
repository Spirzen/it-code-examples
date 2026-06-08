# Числа
x = 42
print(type(x))          # <class 'int'>
print(x.bit_length())   # 6

# Строки
s = "hello"
print(type(s))          # <class 'str'>
print(s.upper())        # HELLO

# Функции
def greet(name):
    return f"Hello, {name}!"

print(type(greet))      # <class 'function'>
greet.description = "Простое приветствие"
print(greet.description)  # Простое приветствие

# Модули

import math

print(type(math))       # <class 'module'>
print(math.sqrt(16))    # 4.0

# Классы
class MyClass:
    pass

print(type(MyClass))    # <class 'type'>
MyClass.version = "1.0"
print(MyClass.version)  # 1.0

# Даже type является объектом
print(type(type))       # <class 'type'>
