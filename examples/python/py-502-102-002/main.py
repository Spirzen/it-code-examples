def sort_file_lines(input_path, output_path):
    try:
        # Чтение файла в память
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        # Удаление лишних переносов строк и фильтрация пустых строк
        clean_lines = [line.strip() for line in lines if line.strip()]
        
        # Сортировка списка по алфавиту
        sorted_lines = sorted(clean_lines)
        
        # Запись отсортированных данных в новый файл
        with open(output_path, 'w', encoding='utf-8') as file:
            for line in sorted_lines:
                file.write(line + '\n')
                
        print(f"Файл успешно обработан. Строк: {len(sorted_lines)}")
        
    except FileNotFoundError:
        print("Ошибка: Файл не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output_sorted.txt"
    sort_file_lines(input_file, output_file)
