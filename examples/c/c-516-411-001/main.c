typedef enum {
    VALUE_INT,
    VALUE_FLOAT
} ValueKind;

typedef struct {
    ValueKind kind;
    union {
        int i;
        float f;
    } data;
} Value;

void print_value(const Value *v) {
    switch (v->kind) {
    case VALUE_INT:
        printf("%d\n", v->data.i);
        break;
    case VALUE_FLOAT:
        printf("%.2f\n", v->data.f);
        break;
    }
}

/* пример вызова:
Value v = {.kind = VALUE_INT, .data.i = 10};
print_value(&v);
*/
