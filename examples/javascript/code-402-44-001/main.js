// Строгое сравнение
if (value === null) {
    // Обработка отсутствия значения
}

// Проверка на отсутствие значения или undefined
if (value == null) {
    // Обрабатывает и null, и undefined
}

// Оператор нулевого слияния (ES2020)
const displayName = userName ?? "Гость";

// Опциональная цепочка вызовов
const city = user?.address?.city ?? "Не указано";
