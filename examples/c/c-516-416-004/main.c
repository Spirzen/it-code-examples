#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
    time_t now = time(NULL);
    struct tm *local = localtime(&now);
    char stamp[64];

    if (local != NULL)
        strftime(stamp, sizeof stamp, "%Y-%m-%d %H:%M:%S", local);

    printf("Сейчас: %s\n", local ? stamp : "?");

    srand((unsigned)time(NULL));
    printf("Кубик: %d\n", rand() % 6 + 1);
    return 0;
}
