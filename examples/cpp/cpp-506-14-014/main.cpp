class Counter {
    int value_ = 0;
public:
    Counter& operator++() {   // префиксный ++
        ++value_;
        return *this;
    }
    Counter operator++(int) {  // постфиксный ++ (фиктивный int)
        Counter old = *this;
        ++value_;
        return old;
    }
    bool operator!() const { return value_ == 0; }
};
