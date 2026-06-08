# Неочевидные сокращения
def calc(a, b, op):
    if op == 1:
        return a + b
    elif op == 2:
        return a - b

# Читаемые имена и константы
OPERATION_ADD = 1
OPERATION_SUBTRACT = 2

def calculate(first_number, second_number, operation):
    if operation == OPERATION_ADD:
        return first_number + second_number
    elif operation == OPERATION_SUBTRACT:
        return first_number - second_number

# Единый интерфейс len() вместо разных свойств
items = [1, 2, 3]
text = "hello"
mapping = {"a": 1, "b": 2}

print(len(items))    # 3
print(len(text))     # 5
print(len(mapping))  # 2
