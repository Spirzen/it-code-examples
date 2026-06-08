void draw() {
    // Очистка поля
    for (int y = 0; y < HEIGHT; y++)
        for (int x = 0; x < WIDTH; x++)
            field[y][x] = ' ';

    // Еда
    field[food_y][food_x] = '*';

    // Змейка: сначала тело, потом голова поверх
    for (int i = 1; i < length; i++)
        field[snake_y[i]][snake_x[i]] = '#';
    field[snake_y[0]][snake_x[0]] = '@';

    // Вывод
    for (int y = 0; y < HEIGHT; y++) {
        for (int x = 0; x < WIDTH; x++)
            putchar(field[y][x]);
        putchar('\n');
    }
}
