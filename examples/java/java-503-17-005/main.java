int number = 42;  // двоичное: 101010
System.out.println(Integer.toBinaryString(number));  // 101010
System.out.println(Integer.bitCount(number));         // 3 — три единицы

int mask = 0b11110000;
System.out.println(Integer.bitCount(mask));           // 4

// Практическое применение: проверка чётности количества единиц
int value = 15;  // 1111
boolean evenOnes = (Integer.bitCount(value) % 2 == 0);
System.out.println("Чётное количество единиц: " + evenOnes);  // true

// Сравнение с ручным подсчётом через битовые операции
int manualCount = 0;
int temp = number;
while (temp != 0) {
    manualCount += temp & 1;
    temp >>>= 1;
}
System.out.println("Ручной подсчёт: " + manualCount);  // 3
