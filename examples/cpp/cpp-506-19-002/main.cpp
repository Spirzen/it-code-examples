class Arena {
    char* start_;
    char* current_;
    size_t capacity_;

public:
    Arena(size_t cap) : capacity_(cap) {
        start_ = static_cast<char*>(::operator new(capacity_));
        current_ = start_;
    }
    ~Arena() { ::operator delete(start_); }

    char* allocate(size_t n) {
        if (current_ + n > start_ + capacity_)
            throw std::bad_alloc{};
        char* p = current_;
        current_ += n;
        return p;
    }

    void reset() { current_ = start_; }  // освобождение "всего сразу"
};

template<typename T>
class ArenaAllocator {
    Arena* arena_;
public:
    using value_type = T;

    ArenaAllocator(Arena& a) : arena_(&a) {}
    template<typename U> ArenaAllocator(const ArenaAllocator<U>& other) : arena_(other.arena_) {}

    T* allocate(size_t n) {
        return reinterpret_cast<T*>(arena_->allocate(n * sizeof(T)));
    }

    void deallocate(T*, size_t) noexcept {
        // ничего не делаем: освобождение — через arena.reset()
    }

    // требуется для совместимости, но не используется
    template<typename U, typename... Args>
    void construct(U* p, Args&&... args) {
        ::new(static_cast<void*>(p)) U(std::forward<Args>(args)...);
    }

    template<typename U>
    void destroy(U* p) {
        p->~U();
    }
};
