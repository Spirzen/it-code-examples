class Counter {
    int start_, end_;
public:
    Counter(int s, int e) : start_(s), end_(e) {}

    struct Iterator {
        int value;
        bool operator!=(const Iterator& other) const { return value != other.value; }
        int operator*() const { return value; }
        Iterator& operator++() { ++value; return *this; }
    };

    Iterator begin() const { return {start_}; }
    Iterator end()   const { return {end_}; }
};

// Использование:
for (int x : Counter(1, 5)) {
    std::cout << x << " ";  // 1 2 3 4
}
