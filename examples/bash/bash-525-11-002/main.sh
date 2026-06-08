# Сохранение вывода команды в файл
ls -la > files.txt

# Добавление вывода к содержимому файла
echo "Новая запись" >> log.txt

# Чтение данных из файла
sort < unsorted_data.txt

# Перенаправление ошибок в отдельный файл
command_that_might_fail 2> error.log

# Перенаправление вывода и ошибок в один файл
command_that_might_fail &> output.log
