from datetime import datetime

def convert_date(date_string, current_format, target_format):
    try:
        # Парсинг входной строки в объект datetime
        date_obj = datetime.strptime(date_string, current_format)
        
        # Форматирование объекта в целевой формат
        result = date_obj.strftime(target_format)
        
        return result
    except ValueError:
        return "Ошибка: Неправильный формат входной даты."

if __name__ == "__main__":
    input_str = "2026-05-06"
    fmt_in = "%Y-%m-%d"
    fmt_out = "%d.%m.%Y %A"
    
    converted = convert_date(input_str, fmt_in, fmt_out)
    print(f"Вход: {input_str} -> Выход: {converted}")
