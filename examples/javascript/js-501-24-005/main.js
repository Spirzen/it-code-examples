// Измерение времени выполнения функции
console.time('fetchData');
fetchData().then(() => {
    console.timeEnd('fetchData');
});

// Мониторинг частоты вызовов
let callCount = 0;
function monitoredFunction() {
    callCount++;
    if (callCount > 1000) {
        console.warn('Функция вызвана слишком часто:', callCount);
    }
    // Основная логика
}
