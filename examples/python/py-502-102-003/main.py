def calculate():
    while True:
        print("\nДоступные операции: +, -, *, / (или 'q' для выхода)")
        operation = input("Выберите операцию: ").strip()
        
        if operation == 'q':
            break
            
        if operation not in ['+', '-', '*', '/']:
            print("Некорректная операция. Попробуйте снова.")
            continue
            
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            
            result = 0
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("Ошибка: Деление на ноль невозможно.")
                    continue
                result = num1 / num2
                
            print(f"Результат: {result}")
            
        except ValueError:
            print("Ошибка: Введите корректные числа.")

if __name__ == "__main__":
    calculate()
