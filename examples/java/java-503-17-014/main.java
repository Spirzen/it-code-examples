int value = 10;

// Цикл while не выполнится
while (value < 5) {
    System.out.println("while: " + value);
    value++;
}

// Цикл do-while выполнится один раз
do {
    System.out.println("do-while: " + value);
    value++;
} while (value < 5);
// Вывод: do-while: 10
