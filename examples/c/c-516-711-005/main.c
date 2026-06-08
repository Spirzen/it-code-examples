// Сохраняем старую голову
int prev_x = snake_x[0];
int prev_y = snake_y[0];

// Обновляем голову
switch (direction) {
    case 'w': snake_y[0]--; break; // вверх
    case 's': snake_y[0]++; break; // вниз
    case 'a': snake_x[0]--; break; // влево
    case 'd': snake_x[0]++; break; // вправо
}

// Сдвигаем тело
for (int i = 1; i < length; i++) {
    int temp_x = snake_x[i];
    int temp_y = snake_y[i];
    snake_x[i] = prev_x;
    snake_y[i] = prev_y;
    prev_x = temp_x;
    prev_y = temp_y;
}
