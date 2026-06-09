"=== user-auth.st — Pharo Playground ==="
Object subclass: #User
    instanceVariableNames: 'username password loggedIn'
    classVariableNames: ''
    package: 'OOPPractice' !

User class >> newUsername: aUser password: aPassword [
    ^ self basicNew
        username: aUser;
        password: aPassword;
        loggedIn: false;
        yourself
]

User >> username: aString [ username := aString ]
User >> password: aString [ password := aString ]
User >> loggedIn: aBoolean [ loggedIn := aBoolean ]

User >> login: aPassword [
    aPassword = password
        ifTrue: [
            loggedIn := true.
            Transcript show: 'Добро пожаловать, ', username, '!'; cr ]
        ifFalse: [
            Transcript show: 'Ошибка: неверный пароль'; cr ]
]

User >> logout [
    loggedIn := false.
    Transcript show: username, ' вышел из системы'; cr
]

User >> postMessage: text [
    loggedIn ifFalse: [
        Transcript show: 'Сначала войдите в систему'; cr.
        ^ self ].
    Transcript show: 'Сообщение опубликовано: ', text; cr
]

"--- Demo ---"
| user |
user := User newUsername: 'alex' password: 'secret123'.
user postMessage: 'Привет!'.
user login: 'wrong'.
user login: 'secret123'.
user postMessage: 'Привет, мир!'.
user logout.
user postMessage: 'Ещё одно сообщение'.
