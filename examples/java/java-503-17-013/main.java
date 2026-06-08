// Чтение данных до достижения конца
boolean hasNext = true;
int dataIndex = 0;
while (hasNext) {
    // обработка данных[dataIndex]
    dataIndex++;
    if (dataIndex >= 10) {
        hasNext = false;  // завершение цикла
    }
}

// Поиск элемента в массиве
int[] items = {4, 8, 15, 16, 23, 42};
int target = 16;
int position = 0;
boolean found = false;

while (position < items.length && !found) {
    if (items[position] == target) {
        found = true;
    } else {
        position++;
    }
}

if (found) {
    System.out.println("Элемент найден на позиции " + position);
}
