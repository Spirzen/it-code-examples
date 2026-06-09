#include <iostream>
#include <string>
#include <vector>
#include <numeric>
#include <iomanip>

class Student {
public:
    static const int PASSING_SCORE = 60;
    std::string name;
    std::vector<int> grades;

    explicit Student(const std::string& name) : name(name) {}

    void add_grade(int grade) {
        grades.push_back(grade);
        std::cout << "Оценка " << grade << " добавлена для " << name << std::endl;
    }

    double average_score() const {
        if (grades.empty()) return 0;
        return static_cast<double>(std::accumulate(grades.begin(), grades.end(), 0)) / grades.size();
    }

    bool is_passing() const {
        return average_score() >= PASSING_SCORE;
    }

    void info() const {
        std::cout << "Студент: " << name << std::endl;
        std::cout << "Оценки: [";
        for (size_t i = 0; i < grades.size(); ++i) {
            if (i > 0) std::cout << ", ";
            std::cout << grades[i];
        }
        std::cout << "]" << std::endl;
        std::cout << std::fixed << std::setprecision(1);
        std::cout << "Средний балл: " << average_score() << std::endl;
        std::cout << (is_passing() ? "Зачёт получен" : "Зачёт не получен") << std::endl;
    }
};

int main() {
    Student student("Анна");
    student.add_grade(70);
    student.add_grade(85);
    student.add_grade(55);
    student.info();
    return 0;
}
