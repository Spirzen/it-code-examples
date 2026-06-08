#include <stdio.h>

int main(void) {
    char buffer[10];
    buffer[0] = 'H';
    buffer[1] = 'e';
    buffer[2] = 'l';
    buffer[3] = 'l';
    buffer[4] = 'o';
    buffer[5] = '\0'; // завершающий нуль — признак конца строки

    printf("Сообщение: %s\n", buffer);
    return 0;
}
