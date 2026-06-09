class Student {
    static final int PASSING_SCORE = 60
    String name
    List<Integer> grades = []

    Student(String name) {
        this.name = name
    }

    void addGrade(int grade) {
        grades << grade
        println "Оценка ${grade} добавлена для ${name}"
    }

    double averageScore() {
        grades.isEmpty() ? 0 : grades.sum() / grades.size()
    }

    boolean isPassing() {
        averageScore() >= PASSING_SCORE
    }

    void info() {
        println "Студент: ${name}"
        println "Оценки: ${grades}"
        println "Средний балл: ${String.format('%.1f', averageScore())}"
        println isPassing() ? 'Зачёт получен' : 'Зачёт не получен'
    }
}

def student = new Student('Анна')
student.addGrade(70)
student.addGrade(85)
student.addGrade(55)
student.info()
