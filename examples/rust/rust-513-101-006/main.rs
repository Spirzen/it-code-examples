let data = vec![1, 2, 3, 4, 5, 6];

// Плохо: создание промежуточных векторов
let result: Vec<_> = data
    .iter()
    .map(|x| x * 2)
    .filter(|x| x % 3 == 0)
    .collect();

// Хорошо: цепочка итераторов без промежуточных аллокаций
let sum: i32 = data
    .iter()
    .map(|x| x * 2)
    .filter(|x| x % 3 == 0)
    .sum();
