public int FactorialTail(int n, int accumulator = 1)
{
    if (n <= 1)
        return accumulator;
    return FactorialTail(n - 1, n * accumulator);
    // Рекурсивный вызов — последняя операция
}
