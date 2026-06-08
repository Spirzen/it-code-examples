#include <type_traits>
#include <iostream>

template<typename T>
void inspectType() {
    if constexpr (std::is_void_v<T>) {
        std::cout << "Тип — void\n";
    } else {
        std::cout << "Тип — не void\n";
    }
}

int main() {
    inspectType<void>();   // Тип — void
    inspectType<int>();    // Тип — не void
    return 0;
}
