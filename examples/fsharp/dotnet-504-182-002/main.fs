// Создание списка
let numbers = [1; 2; 3; 4; 5]

// Добавление элемента в начало
let newList = 0 :: numbers

// Обработка списка с помощью функций высшего порядка
let doubledNumbers = List.map (fun x -> x * 2) numbers
let filteredNumbers = List.filter (fun x -> x > 2) numbers
let sumOfNumbers = List.sum numbers

printfn "Исходный список: %A" numbers
printfn "Удвоенные числа: %A" doubledNumbers
printfn "Числа больше 2: %A" filteredNumbers
printfn "Сумма: %A" sumOfNumbers
