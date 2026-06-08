def process_data(Данные, callback):
    result = [x * 2 for x in Данные]
    callback(result)

def print_result(result):
    print(result)

process_data([1, 2, 3], print_result)  # [2, 4, 6]

# Использование лямбды
process_data([1, 2, 3], lambda r: print(f"Результат: {r}"))
