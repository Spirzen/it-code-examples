#include <stdio.h>
#include <string.h>

struct Book {
    char title[100];
    int pages;
};

int main(void) {
    struct Book b;
    snprintf(b.title, sizeof b.title, "%s", "War and Peace");
    b.pages = 1225;

    printf("Book: %s, pages: %d\n", b.title, b.pages);
    return 0;
}
