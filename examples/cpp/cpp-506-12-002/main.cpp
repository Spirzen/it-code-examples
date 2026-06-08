template<typename T>
class UniquePtr {
    T* ptr_;
public:
    explicit UniquePtr(T* p = nullptr) : ptr_(p) {}
    ~UniquePtr() { delete ptr_; }

    UniquePtr(const UniquePtr&) = delete;
    UniquePtr& operator=(const UniquePtr&) = delete;

    UniquePtr(UniquePtr&& other) noexcept : ptr_(other.ptr_) {
        other.ptr_ = nullptr;
    }

    UniquePtr& operator=(UniquePtr&& other) noexcept {
        if (this != &other) {
            delete ptr_;
            ptr_ = other.ptr_;
            other.ptr_ = nullptr;
        }
        return *this;
    }

    // Операторы разыменования
    T& operator*() const { return *ptr_; }      // возвращает lvalue
    T* operator->() const { return ptr_; }      // возвращает указатель

    // Проверка на "истинность"
    explicit operator bool() const { return ptr_ != nullptr; }

    // Отдача владения
    T* release() noexcept {
        T* p = ptr_;
        ptr_ = nullptr;
        return p;
    }

    void reset(T* p = nullptr) noexcept {
        delete ptr_;
        ptr_ = p;
    }
};
