class Rational {
    int num_, den_;
    static int gcd(int a, int b) { /* … */ }
    void normalize() {
        int g = gcd(num_, den_);
        num_ /= g; den_ /= g;
        if (den_ < 0) { num_ = -num_; den_ = -den_; }
    }
public:
    Rational(int n = 0, int d = 1) : num_(n), den_(d) {
        if (d == 0) throw std::invalid_argument("denominator is zero");
        normalize();
    }

    // Доступ к данным (для оператора)
    int numerator() const { return num_; }
    int denominator() const { return den_; }

    // Перегрузка вывода — как friend
    friend std::ostream& operator<<(std::ostream& os, const Rational& r) {
        if (r.denominator() == 1)
            os << r.numerator();
        else
            os << r.numerator() << '/' << r.denominator();
        return os;
    }

    // Перегрузка ввода — как friend
    friend std::istream& operator>>(std::istream& is, Rational& r) {
        int n, d;
        char slash = 0;
        is >> n;               // читаем числитель
        if (is.peek() == '/') {
            is >> slash >> d;  // читаем '/' и знаменатель
        } else {
            d = 1;             // только целое число — знаменатель 1
        }

        if (is && d != 0) {
            r = Rational(n, d); // конструируем через каноническую форму
        } else {
            is.setstate(std::ios::failbit); // помечаем поток как ошибочный
        }
        return is;
    }
};
