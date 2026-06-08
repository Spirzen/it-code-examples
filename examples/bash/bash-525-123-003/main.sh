# Перенаправить stderr в stdout
command 2>&1

# Перенаправить stdout в файл, stderr в другой файл
command > out.txt 2> err.txt

# Перенаправить оба потока в один файл
command > both.txt 2>&1

# Перенаправить stdin из файла
command < input.txt

# Открыть файл на чтение и запись
exec 3< input.txt
exec 4> output.txt
