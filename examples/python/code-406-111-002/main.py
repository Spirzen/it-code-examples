def process_file(path):
    file = None
    try:
        file = open(path, 'r')
        # Работа с файлом
    except FileNotFoundError as ex:
        print(f"Файл не найден: {ex}")
    finally:
        if file:
            file.close()  # Выполнится всегда
