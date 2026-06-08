
import sys

# 1. Аргументы командной строки
# Запуск — python script.py arg1 arg2
script_name = sys.argv[0]
args = sys.argv[1:]

print(f"Имя скрипта: {script_name}")
print(f"Аргументы: {args}")

if not args:
    print("Предупреждение: аргументы не переданы.")
    sys.exit(1) # Выход с кодом ошибки 1

# 2. Информация о версии и платформе
print(f"Версия Python: {sys.version}")
print(f"Операционная система: {sys.platform}")
print(f"Кодировка по умолчанию: {sys.getdefaultencoding()}")

# 3. Максимальное целое число (арифметика больших чисел)
max_int = sys.maxsize
print(f"Максимальное целое число: {max_int}")

# 4. Перенаправление вывода (пример для логирования)
# sys.stdout = open('log.txt', 'w') 
# print("Это сообщение будет в файле")
# sys.stdout.close()
# sys.stdout = sys.__stdout__ # Возврат к консольному выводу

# 5. Проверка типа данных через sys (редко используется напрямую, но полезно знать)
# Например, проверка, является ли объект потоком ввода
if isinstance(sys.stdin, type(open(0))):
    print("Стандартный ввод доступен.")
