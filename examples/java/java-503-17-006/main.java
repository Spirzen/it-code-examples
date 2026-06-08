String intText = "12345";
int intValue = Integer.parseInt(intText);
System.out.println(intValue);  // 12345

String doubleText = "3.14159";
double doubleValue = Double.parseDouble(doubleText);
System.out.println(doubleValue);  // 3.14159

// Обработка ошибок преобразования
try {
    int invalid = Integer.parseInt("не число");
} catch (NumberFormatException e) {
    System.out.println("Невозможно преобразовать строку в число");
}

// Преобразование с указанием системы счисления
int hexValue = Integer.parseInt("FF", 16);  // 255 в шестнадцатеричной
int binaryValue = Integer.parseInt("1010", 2);  // 10 в двоичной
System.out.println(hexValue);     // 255
System.out.println(binaryValue);  // 10
