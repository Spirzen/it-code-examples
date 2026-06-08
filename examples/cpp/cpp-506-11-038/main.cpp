#include <iostream>

union Payload {
    int i;
    float f;
    char str[20];
};

int main() {
    Payload value{};

    value.i = 10;
    std::cout << "Целое: " << value.i << std::endl;

    value.f = 220.5f;
    std::cout << "Вещественное: " << value.f << std::endl;

    // после записи в f, значение i больше не актуально
    return 0;
}
