#include <concepts>

template<std::integral T>
T abs(T x) {
    return x < 0 ? -x : x;
}

template<std::floating_point T>
T abs(T x) {
    return x < 0 ? -x : x;
}

// Или обобщённо:
template<typename T>
requires std::integral<T> || std::floating_point<T>
T abs(T x) { /* ... */ }
