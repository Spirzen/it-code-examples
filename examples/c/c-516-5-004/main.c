#include <stdio.h>

int main(void) {
    int choice;
    do {
        printf("\n=== Меню ===\n");
        printf("1. Показать приветствие\n");
        printf("2. Показать время\n");
        printf("3. Выход\n");
        printf("Выберите действие: ");
        if (scanf("%d", &choice) != 1) {
            printf("Введите число.\n");
            while (getchar() != '\n' && getchar() != EOF) { }
            choice = 0;
            continue;
        }

        switch (choice) {
            case 1:
                printf("Здравствуйте!\n");
                break;
            case 2:
                printf("Текущее время: [заглушка]\n");
                break;
            case 3:
                printf("Выход...\n");
                break;
            default:
                printf("Неверный выбор. Попробуйте снова.\n");
        }
    } while (choice != 3);

    return 0;
}
