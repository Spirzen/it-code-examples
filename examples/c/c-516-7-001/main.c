#include <stdio.h>

int main(void)
{
    char name[64];
    printf("Введите имя: ");

    if (fgets(name, sizeof name, stdin) == NULL) {
        fprintf(stderr, "Ошибка чтения ввода\n");
        return 1;
    }

    printf("Привет, %s", name);
    return 0;
}
