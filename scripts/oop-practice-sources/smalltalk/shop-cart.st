"=== shop-cart.st — Pharo Playground ==="
Object subclass: #Product
    instanceVariableNames: 'name price'
    classVariableNames: ''
    package: 'OOPPractice' !

Product class >> newName: aName price: aPrice [
    ^ self basicNew
        name: aName;
        price: aPrice;
        yourself
]

Product >> name: aString [ name := aString ]
Product >> price: anInteger [ price := anInteger ]

Object subclass: #Cart
    instanceVariableNames: 'items'
    classVariableNames: ''
    package: 'OOPPractice' !

Cart class >> new [
    ^ self basicNew items: OrderedCollection new; yourself
]

Cart >> items: aCollection [ items := aCollection ]

Cart >> add: product [
    items add: product.
    Transcript show: 'В корзину добавлено: ', product name, ' (', product price printString, ' ₽)'; cr
]

Cart >> total [
    ^ items inject: 0 into: [ :sum :p | sum + p price ]
]

Object subclass: #Order
    instanceVariableNames: 'items total'
    classVariableNames: ''
    package: 'OOPPractice' !

Order class >> fromCart: aCart [
    ^ self basicNew
        items: aCart items copy;
        total: aCart total;
        yourself
]

Order >> checkout [
    Transcript show: 'Оформление заказа...'; cr.
    items do: [ :item |
        Transcript show: '  — ', item name, ': ', item price printString, ' ₽'; cr ].
    Transcript show: 'Итого: ', total printString, ' ₽'; cr.
    Transcript show: 'Заказ оформлен!'; cr
]

"--- Demo ---"
| cart order |
cart := Cart new.
cart add: (Product newName: 'Книга' price: 500).
cart add: (Product newName: 'Ручка' price: 50).
order := Order fromCart: cart.
order checkout.
