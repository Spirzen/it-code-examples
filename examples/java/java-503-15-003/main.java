// Неправильный подход — использование double для денег
double price1 = 0.1;
double price2 = 0.2;
double total = price1 + price2;
System.out.println(total); // 0.30000000000000004 — погрешность!

// Правильный подход — BigDecimal
BigDecimal a = new BigDecimal("0.1");
BigDecimal b = new BigDecimal("0.2");
BigDecimal sum = a.add(b);
System.out.println(sum); // 0.3 — точный результат

// Операции с округлением
BigDecimal quantity = new BigDecimal("3");
BigDecimal unitPrice = new BigDecimal("1.333");
BigDecimal totalPrice = unitPrice.multiply(quantity)
    .setScale(2, RoundingMode.HALF_UP); // 4.00

// Сравнение значений
BigDecimal x = new BigDecimal("10.00");
BigDecimal y = new BigDecimal("10.0");
System.out.println(x.equals(y));   // false — scale различается
System.out.println(x.compareTo(y) == 0); // true — числовое равенство

// Создание из примитивов и строк
BigDecimal fromInt = BigDecimal.valueOf(100);      // 100
BigDecimal fromDouble = BigDecimal.valueOf(123.45); // 123.45
BigDecimal fromString = new BigDecimal("999.99");   // 999.99
