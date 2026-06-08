String text1 = new String("привет");
String text2 = new String("привет");
String text3 = "привет";

System.out.println(text1 == text2);        // false — разные объекты в памяти
System.out.println(text1.equals(text2));   // true — одинаковое содержимое
System.out.println(text1.equals(text3));   // true — содержимое совпадает

Integer num1 = 100;
Integer num2 = 100;
System.out.println(num1 == num2);          // true — кэширование малых целых чисел
System.out.println(num1.equals(num2));     // true

Integer big1 = 200;
Integer big2 = 200;
System.out.println(big1 == big2);          // false — разные объекты
System.out.println(big1.equals(big2));     // true — содержимое одинаковое
