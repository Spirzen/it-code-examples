// Рекурсия
function factorial(n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

// Цикл
function factorial(n) {
    let result = 1;
    for (let i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}
