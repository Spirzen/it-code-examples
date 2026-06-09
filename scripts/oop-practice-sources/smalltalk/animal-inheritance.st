"=== animal-inheritance.st — Pharo Playground ==="
Object subclass: #Animal
    instanceVariableNames: 'name'
    classVariableNames: ''
    package: 'OOPPractice' !

Animal class >> newName: aName [
    ^ self basicNew name: aName; yourself
]

Animal >> name: aString [ name := aString ]

Animal >> eat [
    Transcript show: name, ' ест'; cr
]

Object subclass: #Cat
    instanceVariableNames: ''
    classVariableNames: ''
    package: 'OOPPractice' !

Cat >> speak [
    Transcript show: 'Мяу!'; cr
]

Object subclass: #Dog
    instanceVariableNames: ''
    classVariableNames: ''
    package: 'OOPPractice' !

Dog >> speak [
    Transcript show: 'Гав!'; cr
]

"--- Demo ---"
| cat dog |
cat := Cat newName: 'Мурка'.
dog := Dog newName: 'Шарик'.
cat eat.
cat speak.
dog eat.
dog speak.
