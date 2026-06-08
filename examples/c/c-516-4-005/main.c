#include <stdio.h>
#include <string.h>

struct Student {
    char name[30];
    int grade;
};

void print_top_students(struct Student students[], int count) {
    for (int i = 0; i < count; i++) {
        if (students[i].grade >= 90) {
            printf("Отличник: %s (оценка: %d)\n", students[i].name, students[i].grade);
        }
    }
}

int main(void) {
    struct Student group[] = {
        {"Иван", 85},
        {"Мария", 95},
        {"Анна", 92}
    };
    int size = sizeof(group) / sizeof(group[0]);

    print_top_students(group, size);
    return 0;
}
