function calculateSum(a, b) {
    // 'a' и 'b' — имена параметров, разрешаемые в области видимости функции
    return a + b;
}

let result = calculateSum(2, 3);
console.log(result); // 5

// Попытка доступа к параметру за пределами функции вызовет ошибку
try {
    console.log(a); 
} catch (e) {
    console.error("Ошибка:", e.message); // ReferenceError: a is not defined
}
