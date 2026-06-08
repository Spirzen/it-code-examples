int age = 25;
boolean hasLicense = true;

if (age >= 18 && hasLicense) {
    System.out.println("Можно водить автомобиль");
}

String role = "admin";
if (role.equals("admin") || role.equals("moderator")) {
    System.out.println("Доступ к административным функциям");
}

boolean isWeekend = true;
if (!isWeekend) {
    System.out.println("Рабочий день");
} else {
    System.out.println("Выходной");  // выполняется эта ветка
}
