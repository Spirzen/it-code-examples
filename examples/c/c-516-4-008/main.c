#include <stdio.h>

int string_length(char* s) {
    int len = 0;
    while (*s != '\0') {
        len++;
        s++;
    }
    return len;
}

int main(void) {
    char text[] = "С — язык близкий к железу";
    int len = string_length(text);
    printf("Длина строки: %d символов\n", len);
    return 0;
}
