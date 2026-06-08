class Sensor {
private:
    double raw_value;

protected:
    void calibrate() { /* внутренняя логика калибровки */ }

public:
    double getValue() const { return raw_value * 0.98; }
    
    friend void diagnosticsTool(const Sensor& s); // разрешаем доступ в диагностике
};

void diagnosticsTool(const Sensor& s) {
    std::cout << "Raw: " << s.raw_value << "\n"; // допустимо благодаря friend
}
