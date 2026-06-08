String a = "яблоко";
String b = "апельсин";
System.out.println(a.compareTo(b));  // положительное число — "яблоко" позже в алфавите

String c = "банан";
System.out.println(b.compareTo(c));  // отрицательное число — "апельсин" раньше "банана"

Integer x = 42;
Integer y = 17;
System.out.println(x.compareTo(y));  // положительное число — 42 больше 17

// Сортировка списка с использованием compareTo
List<String> fruits = Arrays.asList("груша", "яблоко", "апельсин", "банан");
fruits.sort(String::compareTo);
System.out.println(fruits);  // [апельсин, банан, груша, яблоко]
