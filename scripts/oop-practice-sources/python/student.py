class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.id = student_id
        self.grades = []   # Список оценок (пустой изначально)

    def add_grade(self, subject, score):
        """Добавить оценку по предмету"""
        if 0 <= score <= 100:
            self.grades.append({"subject": subject, "score": score})
            print(f"{self.name} получил {score} по {subject}")
        else:
            print("Оценка должна быть от 0 до 100!")

    def average_score(self):
        if not self.grades:  # Если список пуст
            return 0
        total = sum(grade["score"] for grade in self.grades)
        return total / len(self.grades)

    def is_passing(self):
        """Проходной балл 60"""
        return self.average_score() >= 60

    def info(self):
        avg = self.average_score()
        status = "Сдал" if self.is_passing() else "Не сдал"
        print(f"Студент: {self.name} (ID: {self.id})")
        print(f"Средний балл: {avg:.1f} - {status}")


# Создаем студентов
alice = Student("Алиса", "S001")
bob = Student("Боб", "S002")

alice.add_grade("Математика", 85)
alice.add_grade("Физика", 72)
alice.info()
# Вывод:
# Студент: Алиса (ID: S001)
# Средний балл: 78.5 - Сдал

bob.add_grade("Математика", 45)
bob.add_grade("Физика", 50)
bob.info()
# Средний балл: 47.5 - Не сдал
