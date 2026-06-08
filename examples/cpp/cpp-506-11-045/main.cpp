// Вспомогательный trait: имеет ли T метод void serialize() const?
template<typename T, typename = void>
struct has_serialize : std::false_type {};

template<typename T>
struct has_serialize<T, std::void_t<decltype(std::declval<const T&>().serialize())>>
    : std::true_type {};

// Перегрузки:
template<typename T>
std::enable_if_t<has_serialize_v<T>> save(const T& obj) {
    obj.serialize(); // безопасно — перегрузка доступна только если serialize существует
}

template<typename T>
std::enable_if_t<!has_serialize_v<T>> save(const T& obj) {
    // fallback: например, бинарная запись
    write_bytes(reinterpret_cast<const char*>(&obj), sizeof(obj));
}
