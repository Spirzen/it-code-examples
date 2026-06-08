# По списку
for item in list_of_items; do
    echo "$item"
done

# С использованием glob
for file in *.txt; do
    echo "Обработка: $file"
done

# Классический цикл C
for (( i=0; i<10; i++ )); do
    echo "Счетчик: $i"
done
