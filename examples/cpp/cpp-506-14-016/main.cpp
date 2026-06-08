#include <type_traits>

// Вызывается, только если T — целочисленный тип
template<typename T>
typename std::enable_if<std::is_integral_v<T>, T>::type
abs(T x) {
    return x < 0 ? -x : x;
}

// Вызывается для остальных типов (например, float, double)
template<typename T>
typename std::enable_if<!std::is_integral_v<T>, T>::type
abs(T x) {
    return x < 0 ? -x : x;
}
