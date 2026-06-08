// Прямое присваивание значений
boolean isActive = true;         // пользователь активен
boolean isAdmin = false;         // пользователь не администратор
boolean hasPermission = true;    // разрешение предоставлено

// Результат логических операций
boolean andResult = true && false;   // false — логическое И
boolean orResult = true || false;    // true — логическое ИЛИ
boolean notResult = !true;           // false — логическое НЕ
boolean xorResult = true ^ false;    // true — исключающее ИЛИ

// Результат сравнений
boolean isEqual = (10 == 10);        // true
boolean isGreater = (15 > 10);       // true
boolean isLessOrEqual = (5 <= 5);    // true
boolean isNotEqual = (7 != 8);       // true

// Использование в условных конструкциях
if (isActive && hasPermission) {
    System.out.println("Доступ разрешён");
}

// Массив булевых значений
boolean[] flags = {true, false, true, false};
boolean allTrue = flags[0] && flags[2]; // true

// Обёртка Boolean с разделяемыми константами
Boolean boxedTrue = Boolean.TRUE;    // ссылка на разделяемый объект
Boolean boxedFalse = Boolean.FALSE;  // ссылка на разделяемый объект
Boolean parsed = Boolean.parseBoolean("true"); // true
