struct Student {
    name: String,
    grades: Vec<i32>,
}

impl Student {
    const PASSING_SCORE: i32 = 60;

    fn new(name: &str) -> Self {
        Self {
            name: name.to_string(),
            grades: Vec::new(),
        }
    }

    fn add_grade(&mut self, grade: i32) {
        self.grades.push(grade);
        println!("Оценка {} добавлена для {}", grade, self.name);
    }

    fn average_score(&self) -> f64 {
        if self.grades.is_empty() {
            return 0.0;
        }
        let sum: i32 = self.grades.iter().sum();
        sum as f64 / self.grades.len() as f64
    }

    fn is_passing(&self) -> bool {
        self.average_score() >= Self::PASSING_SCORE as f64
    }

    fn info(&self) {
        println!("Студент: {}", self.name);
        println!("Оценки: {:?}", self.grades);
        println!("Средний балл: {:.1}", self.average_score());
        if self.is_passing() {
            println!("Зачёт получен");
        } else {
            println!("Зачёт не получен");
        }
    }
}

fn main() {
    let mut student = Student::new("Анна");
    student.add_grade(70);
    student.add_grade(85);
    student.add_grade(55);
    student.info();
}
