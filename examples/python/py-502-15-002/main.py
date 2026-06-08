# Неявное состояние через глобальную переменную
counter = 0

def increment():
    global counter
    counter += 1

# Явное управление состоянием
def increment(counter):
    return counter + 1

current = 0
current = increment(current)

# Python — явное преобразование
value = int("42")

# Perl-подобный подход (неявное) — $value = "42" + 0
