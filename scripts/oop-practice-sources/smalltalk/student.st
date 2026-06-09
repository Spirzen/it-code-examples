"=== student.st — Pharo Playground ==="
Object subclass: #Student
    instanceVariableNames: 'name grades'
    classVariableNames: 'PassingScore'
    package: 'OOPPractice' !

Student class >> initialize [
    PassingScore := 60
]

Student class >> newName: aName [
    ^ self basicNew
        name: aName;
        grades: OrderedCollection new;
        yourself
]

Student >> name: aString [ name := aString ]
Student >> grades: aCollection [ grades := aCollection ]

Student >> addGrade: grade [
    grades add: grade.
    Transcript show: 'Оценка ', grade printString, ' добавлена для ', name; cr
]

Student >> averageScore [
    grades isEmpty ifTrue: [ ^ 0 ].
    ^ (grades sum) / grades size
]

Student >> isPassing [
    ^ self averageScore >= PassingScore
]

Student >> info [
    Transcript show: 'Студент: ', name; cr.
    Transcript show: 'Оценки: ', grades printString; cr.
    Transcript show: 'Средний балл: ', (self averageScore printShowingDecimalPlaces: 1); cr.
    Transcript show: (self isPassing ifTrue: ['Зачёт получен'] ifFalse: ['Зачёт не получен']); cr
]

"--- Demo ---"
| student |
student := Student newName: 'Анна'.
student addGrade: 70.
student addGrade: 85.
student addGrade: 55.
student info.
