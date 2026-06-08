// Общая версия
template<typename T>
struct Printer {
    static void print(const T& x) {
        std::cout << x << '\n';
    }
};

// Специализация для bool
template<>
struct Printer<bool> {
    static void print(bool x) {
        std::cout << (x ? "true" : "false") << '\n';
    }
};

Printer<int>::print(42);     // 42
Printer<bool>::print(true);  // true
