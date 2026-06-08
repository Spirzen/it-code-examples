#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node *next;
} Node;

Node *head = NULL;
Node *n = malloc(sizeof *n);
if (n != NULL) {
    n->data = 42;
    n->next = head;
    head = n;
}
