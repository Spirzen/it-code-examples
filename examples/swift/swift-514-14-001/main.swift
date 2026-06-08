let a = 10, b = 3
let sum = a + b                    // 13
let isEven = a % 2 == 0            // Bool: false

let isLoggedIn = true
let isAdmin = false
let isGuest = true
let canEdit = isLoggedIn && isAdmin
let hasAccess = isLoggedIn || isGuest

var counter = 0
counter += 1                       // составное присваивание

let label = isEven ? "чётное" : "нечётное"
let indices = 0..<5                // 0, 1, 2, 3, 4
let page = 1...3                   // 1, 2, 3 включительно
