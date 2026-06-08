// Функция принимает массив и функцию-предикат
function filterArray(arr, predicate) {
    const result = [];
    for (const item of arr) {
        if (predicate(item)) {
            result.push(item);
        }
    }
    return result;
}

// Используем с анонимной функцией
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

//Обратите внимание - здесь функция filterArray вызывается
const evens = filterArray(numbers, function(x) {
    return x % 2 === 0;
    // Эта функция не имеет имени и передаётся как аргумент в параметр predicate
});

console.log(evens); // [2, 4, 6, 8, 10]
