// Одномерные массивы примитивов
int[] numbers = new int[5];      // массив из 5 целых чисел, все 0
numbers[0] = 10;                 // присваивание значения первому элементу
numbers[1] = 20;

int[] initialized = {1, 2, 3, 4, 5}; // инициализация при объявлении
int length = initialized.length;     // 5 — длина массива

// Массивы ссылочных типов
String[] names = new String[3];  // массив из 3 ссылок, все null
names[0] = "Алексей";
names[1] = "Мария";
names[2] = "Дмитрий";

String[] cities = {"Москва", "Санкт-Петербург", "Казань"};

// Двумерные массивы (массивы массивов)
int[][] matrix = new int[3][3];  // матрица 3x3
matrix[0][0] = 1;
matrix[0][1] = 2;
matrix[0][2] = 3;

int[][] jagged = new int[3][];   // зубчатый массив
jagged[0] = new int[2];          // первая строка длиной 2
jagged[1] = new int[4];          // вторая строка длиной 4
jagged[2] = new int[3];          // третья строка длиной 3

// Итерация по массиву
for (int i = 0; i < numbers.length; i++) {
    System.out.println(numbers[i]);
}

// Улучшенный цикл for
for (String name : names) {
    System.out.println(name);
}

// Копирование массива
int[] source = {1, 2, 3, 4, 5};
int[] destination = new int[5];
System.arraycopy(source, 0, destination, 0, source.length);
// destination теперь содержит {1, 2, 3, 4, 5}
