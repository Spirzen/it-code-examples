#include <stdio.h>
#include <stdlib.h>

int main() {
    int* numbers = (int*)malloc(3 * sizeof(int));
    if (numbers == NULL) {
        fprintf(stderr, "Ошибка выделения памяти\n");
        return 1;
    }

    numbers[0] = 10;
    numbers[1] = 20;
    numbers[2] = 30;

    printf("Сумма: %d\n", numbers[0] + numbers[1] + numbers[2]);

    free(numbers);
    return 0;
}
