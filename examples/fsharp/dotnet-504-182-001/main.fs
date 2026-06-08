open System

// Объявление начальных значений
let mutable count = 0
let mutable name = ""

// Функция отображения приветствия
let displayGreeting () =
    if String.IsNullOrEmpty(name) then
        printfn "Привет, мир!"
    else
        printfn "Привет, %s! 👋" name

// Функция обработки ввода имени
let inputName () =
    printf "Введите ваше имя: "
    let input = Console.ReadLine()
    match input with
    | null | "" -> name <- ""
    | _ -> name <- input.Trim()

// Функция увеличения счетчика
let increment () =
    count <- count + 1

// Функция уменьшения счетчика
let decrement () =
    if count > 0 then
        count <- count - 1

// Функция сброса счетчика
let reset () =
    count <- 0

// Основная функция запуска приложения
let rec mainLoop () =
    printf "\n=== Счетчик ===\n"
    printf "Счетчик: %d\n" count
    printf "Выберите действие:\n"
    printf "1. Ввести имя\n"
    printf "2. Увеличить (+)\n"
    printf "3. Уменьшить (-)\n"
    printf "4. Сбросить (0)\n"
    printf "5. Выйти\n"
    printf "Ваш выбор: "
    
    let choice = Console.ReadLine()
    
    match choice with
    | "1" -> inputName(); mainLoop ()
    | "2" -> increment(); mainLoop ()
    | "3" -> decrement(); mainLoop ()
    | "4" -> reset(); mainLoop ()
    | "5" -> printfn "До свидания!"; ()
    | _ -> printfn "Неверный ввод. Попробуйте снова."; mainLoop ()

[<EntryPoint>]
let main argv =
    displayGreeting ()
    mainLoop ()
    0 // Код возврата
