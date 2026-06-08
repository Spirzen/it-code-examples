#include <iostream>
#include <limits>

int main() {
    std::cout << "sizeof(float)       = " << sizeof(float)       << " bytes\n";
    std::cout << "sizeof(double)      = " << sizeof(double)      << " bytes\n";
    std::cout << "sizeof(long double) = " << sizeof(long double) << " bytes\n";

    std::cout << "\nДиапазоны:\n";
    std::cout << "float:  [" << std::numeric_limits<float>::min() << ", " 
              << std::numeric_limits<float>::max() << "]\n";
    std::cout << "double: [" << std::numeric_limits<double>::min() << ", " 
              << std::numeric_limits<double>::max() << "]\n";

    std::cout << "\nТочность (количество десятичных цифр):\n";
    std::cout << "float:  " << std::numeric_limits<float>::digits10 << '\n';
    std::cout << "double: " << std::numeric_limits<double>::digits10 << '\n';

    return 0;
}
