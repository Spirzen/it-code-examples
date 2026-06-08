public int Factorial(int n)
{
    if (n <= 1)
        return 1;
    return n * Factorial(n - 1);
}

// Вызов Factorial(5):
// Factorial(5) = 5 * Factorial(4)
//              = 5 * 4 * Factorial(3)
//              = 5 * 4 * 3 * Factorial(2)
//              = 5 * 4 * 3 * 2 * Factorial(1)
//              = 5 * 4 * 3 * 2 * 1 = 120
