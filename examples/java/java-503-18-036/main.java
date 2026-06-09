import java.util.ArrayList;

class Student {
    static final int PASSING_SCORE = 60;
    String name;
    ArrayList<Integer> grades = new ArrayList<>();

    Student(String name) {
        this.name = name;
    }

    void addGrade(int grade) {
        grades.add(grade);
        System.out.println("Оценка " + grade + " добавлена для " + name);
    }

    double averageScore() {
        if (grades.isEmpty()) return 0;
        int sum = 0;
        for (int g : grades) sum += g;
        return (double) sum / grades.size();
    }

    boolean isPassing() {
        return averageScore() >= PASSING_SCORE;
    }

    void info() {
        System.out.println("Студент: " + name);
        System.out.println("Оценки: " + grades);
        System.out.printf("Средний балл: %.1f%n", averageScore());
        System.out.println(isPassing() ? "Зачёт получен" : "Зачёт не получен");
    }
}

public class Main {
    public static void main(String[] args) {
        Student student = new Student("Анна");
        student.addGrade(70);
        student.addGrade(85);
        student.addGrade(55);
        student.info();
    }
}
