#include <stdio.h>

// Объявление функции
int square(int n);

int main(void)
{
    int value = square(4);
    printf("Квадрат числа: %d\n", value);
    return 0;
}

// Определение функции
int square(int n)
{
    return n * n;
}
