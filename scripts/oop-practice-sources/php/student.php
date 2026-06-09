<?php

class Student
{
    public const PASSING_SCORE = 60;

    /** @var list<int> */
    private array $grades = [];

    public function __construct(private string $name) {}

    public function addGrade(int $grade): void
    {
        $this->grades[] = $grade;
        echo "Оценка {$grade} добавлена для {$this->name}\n";
    }

    public function averageScore(): float
    {
        if ($this->grades === []) {
            return 0;
        }
        return array_sum($this->grades) / count($this->grades);
    }

    public function isPassing(): bool
    {
        return $this->averageScore() >= self::PASSING_SCORE;
    }

    public function info(): void
    {
        $avg = $this->averageScore();
        $status = $this->isPassing() ? 'Зачёт получен' : 'Зачёт не получен';
        echo "Студент: {$this->name}\n";
        echo 'Оценки: [' . implode(', ', $this->grades) . "]\n";
        echo 'Средний балл: ' . number_format($avg, 1) . "\n";
        echo "{$status}\n";
    }
}

$student = new Student('Анна');
$student->addGrade(70);
$student->addGrade(85);
$student->addGrade(55);
$student->info();
