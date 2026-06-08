int max = Integer.MAX_VALUE;  // 2147483647
System.out.println(max + 1);  // -2147483648 — тихое переполнение

try {
    int result = Math.addExact(max, 1);
    System.out.println(result);
} catch (ArithmeticException e) {
    System.out.println("Переполнение при сложении: " + e.getMessage());
}

long big = Long.MAX_VALUE;
try {
    long product = Math.multiplyExact(big, 2);
} catch (ArithmeticException e) {
    System.out.println("Переполнение при умножении");
}

// Безопасное вычитание
int safeSubtract = Math.subtractExact(100, 50);
System.out.println(safeSubtract);  // 50
