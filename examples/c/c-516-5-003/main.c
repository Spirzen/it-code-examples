#include <stdio.h>

int main(void) {
    int numbers[] = {34, 12, 78, 5, 92, 23};
    int size = sizeof(numbers) / sizeof(numbers[0]);

    int max = numbers[0];  // предполагаем, что первый — максимум
    for (int i = 1; i < size; i++) {
        if (numbers[i] > max) {
            max = numbers[i];
        }
    }

    printf("Максимальное значение: %d\n", max);
    return 0;
}
