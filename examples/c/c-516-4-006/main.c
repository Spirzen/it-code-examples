#include <stdio.h>
#include <string.h>

union Value {
    int integer;
    float real;
};

int main(void) {
    union Value v;
    v.integer = 42;
    printf("Целое: %d\n", v.integer);

    v.real = 3.14f;
    printf("Вещественное: %.2f\n", v.real);
    // Значение integer теперь недействительно
    return 0;
}
