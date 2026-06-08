#define READ   0b001  // 1
#define WRITE  0b010  // 2
#define EXEC   0b100  // 4

int permissions = READ | WRITE;  // разрешено чтение и запись

// Проверка: есть ли право на запись?
if (permissions & WRITE) {
    printf("Запись разрешена.\n");
}

// Добавление права на выполнение
permissions |= EXEC;

// Запрет записи
permissions &= ~WRITE;
