#include <stdio.h>

union ByteView {
    unsigned int num;
    unsigned char bytes[4];
};

int main(void) {
    union ByteView view;
    view.num = 0x12345678;

    printf("Байты (младший к старшему): ");
    for (int i = 0; i < 4; i++) {
        printf("%02X ", view.bytes[i]);
    }
    printf("\n");
    return 0;
}
