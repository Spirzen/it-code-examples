Scanner scanner = new Scanner(System.in);

// Чтение строк
String str = scanner.nextLine();      // вся строка целиком
String word = scanner.next();         // только до пробела

// Чтение чисел
byte b = scanner.nextByte();          // byte
short sh = scanner.nextShort();       // short
int i = scanner.nextInt();            // int
long l = scanner.nextLong();          // long
float f = scanner.nextFloat();        // float
double d = scanner.nextDouble();      // double

// Проверка наличия данных
if (scanner.hasNextInt()) {           // проверка, можно ли прочитать int
    int num = scanner.nextInt();
}
