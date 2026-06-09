"=== smartphone.st — Pharo Playground ==="
Object subclass: #Smartphone
    instanceVariableNames: 'model battery'
    classVariableNames: ''
    package: 'OOPPractice' !

Smartphone class >> newModel: aModel [
    ^ self basicNew
        model: aModel;
        battery: 20;
        yourself
]

Smartphone >> model: aString [ model := aString ]
Smartphone >> battery: anInteger [ battery := anInteger ]

Smartphone >> call [
    battery := (battery - 5) max: 0.
    Transcript show: 'Звонок с ', model, '... Заряд: ', battery printString, '%'; cr
]

Smartphone >> charge [
    battery := (battery + 30) min: 100.
    Transcript show: 'Зарядка ', model, '... Заряд: ', battery printString, '%'; cr
]

Smartphone >> showStatus [
    Transcript show: 'Смартфон ', model, ': заряд ', battery printString, '%'; cr
]

"--- Demo ---"
| phone |
phone := Smartphone newModel: 'Pixel'.
phone showStatus.
phone call.
phone charge.
phone showStatus.
