"=== bank-account.st — Pharo Playground ==="
Object subclass: #BankAccount
    instanceVariableNames: 'owner balance'
    classVariableNames: ''
    package: 'OOPPractice' !

BankAccount class >> newOwner: aName [
    ^ self basicNew
        owner: aName;
        balance: 1000;
        yourself
]

BankAccount >> owner: aString [ owner := aString ]
BankAccount >> balance: anInteger [ balance := anInteger ]

BankAccount >> deposit: amount [
    balance := balance + amount.
    Transcript show: 'Пополнение: +', amount printString, ' ₽. Баланс: ', balance printString, ' ₽'; cr
]

BankAccount >> withdraw: amount [
    amount > balance ifTrue: [
        Transcript show: 'Ошибка: недостаточно средств'; cr.
        ^ self ].
    balance := balance - amount.
    Transcript show: 'Снятие: -', amount printString, ' ₽. Баланс: ', balance printString, ' ₽'; cr
]

BankAccount >> showBalance [
    Transcript show: 'Текущий баланс: ', balance printString, ' ₽'; cr
]

"--- Demo ---"
| account |
account := BankAccount newOwner: 'Иван'.
account deposit: 500.
account withdraw: 200.
account showBalance.
Transcript show: 'Попытка прямого доступа к балансу...'; cr.
[ account balance ]
    on: MessageNotUnderstood do: [ :ex |
        Transcript show: 'Ошибка: прямой доступ к балансу запрещён'; cr ].
account showBalance.
