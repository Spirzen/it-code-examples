"=== figure.st — Pharo Playground ==="
Object subclass: #Figure
    instanceVariableNames: 'name color'
    classVariableNames: ''
    package: 'OOPPractice' !

Figure class >> newName: aName color: aColor [
    ^ self basicNew
        name: aName;
        color: aColor;
        yourself
]

Figure >> name: aString [ name := aString ]
Figure >> color: aString [ color := aString ]

Figure >> describe [
    Transcript show: 'Фигура «', name, '», цвет: ', color; cr
]

Object subclass: #Circle
    instanceVariableNames: ''
    classVariableNames: ''
    package: 'OOPPractice' !

Circle class >> newColor: aColor [
    ^ (Figure newName: 'Круг' color: aColor)
]

Object subclass: #Square
    instanceVariableNames: ''
    classVariableNames: ''
    package: 'OOPPractice' !

Square class >> newColor: aColor [
    ^ (Figure newName: 'Квадрат' color: aColor)
]

"--- Demo ---"
| circle square |
circle := Circle newColor: 'красный'.
square := Square newColor: 'синий'.
circle describe.
square describe.
