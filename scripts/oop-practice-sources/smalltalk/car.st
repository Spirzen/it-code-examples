"=== car.st — Pharo Playground ==="
Object subclass: #Car
    instanceVariableNames: 'brand fuel mileage'
    classVariableNames: 'ServiceInterval FuelPerKm'
    package: 'OOPPractice' !

Car class >> initialize [
    ServiceInterval := 15000.
    FuelPerKm := 0.1
]

Car class >> newBrand: aBrand [
    ^ self basicNew
        brand: aBrand;
        fuel: 40.0;
        mileage: 0;
        yourself
]

Car >> brand: aString [ brand := aString ]
Car >> fuel: aFloat [ fuel := aFloat ]
Car >> mileage: anInteger [ mileage := anInteger ]

Car >> refuel: liters [
    fuel := fuel + liters.
    Transcript show: 'Заправка: +', liters printString, ' л. Топливо: ',
        (fuel printShowingDecimalPlaces: 1), ' л'; cr
]

Car >> drive: km [
    | needed |
    needed := km * FuelPerKm.
    needed > fuel ifTrue: [
        Transcript show: 'Ошибка: недостаточно топлива'; cr.
        ^ self ].
    fuel := fuel - needed.
    mileage := mileage + km.
    Transcript show: 'Проехали ', km printString, ' км. Топливо: ',
        (fuel printShowingDecimalPlaces: 1), ' л. Пробег: ', mileage printString, ' км'; cr.
    mileage >= ServiceInterval ifTrue: [
        Transcript show: '⚠️ ВНИМАНИЕ: требуется техобслуживание!'; cr ]
]

"--- Demo ---"
| car |
car := Car newBrand: 'Lada'.
car refuel: 10.
car drive: 5000.
car drive: 11000.
