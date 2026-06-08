#include <stdio.h>

int main(void) {
    int age;
    do {
        printf("Введите ваш возраст (0–120): ");
        if (scanf("%d", &age) != 1) {
            printf("Нужно целое число.\n");
            while (getchar() != '\n' && getchar() != EOF) { }
            age = -1;
            continue;
        }
    } while (age < 0 || age > 120);

    printf("Ваш возраст: %d\n", age);
    return 0;
}
