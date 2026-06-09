class Student {
    static let passingScore = 60
    let name: String
    private var grades: [Int] = []

    init(name: String) {
        self.name = name
    }

    func addGrade(_ grade: Int) {
        grades.append(grade)
        print("Оценка \(grade) добавлена для \(name)")
    }

    func averageScore() -> Double {
        guard !grades.isEmpty else { return 0 }
        return Double(grades.reduce(0, +)) / Double(grades.count)
    }

    func isPassing() -> Bool {
        averageScore() >= Double(Self.passingScore)
    }

    func info() {
        print("Студент: \(name)")
        print("Оценки: \(grades)")
        print(String(format: "Средний балл: %.1f", averageScore()))
        print(isPassing() ? "Зачёт получен" : "Зачёт не получен")
    }
}

let student = Student(name: "Анна")
student.addGrade(70)
student.addGrade(85)
student.addGrade(55)
student.info()
