# Список
for item in [1, 2, 3]:
    print(item)

# Словарь — итерация по ключам, как у других коллекций
for key in {"a": 1, "b": 2}:
    print(key)

# Строка — итерация по символам
for char in "text":
    print(char)

# Генератор — тот же протокол итерации
def generate():
    yield 1
    yield 2

for value in generate():
    print(value)
