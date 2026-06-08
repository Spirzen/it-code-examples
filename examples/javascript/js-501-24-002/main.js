// Базовый вывод
console.log('Обычное сообщение');
console.info('Информационное сообщение');
console.warn('Предупреждение');
console.error('Ошибка');

// Вывод с форматированием
console.log('Значение переменной: %s', variable);
console.log('Число: %d, Строка: %s', 42, 'test');

// Вывод объектов и таблиц
console.table([{name: 'John', age: 30}, {name: 'Jane', age: 25}]);
console.dir(document.body);

// Группировка сообщений
console.group('Группа сообщений');
console.log('Сообщение 1');
console.log('Сообщение 2');
console.groupEnd();

// Измерение времени выполнения
console.time('operation');
// Код для измерения
console.timeEnd('operation');

// Подсчёт вызовов
console.count('counter');
console.count('counter');
console.countReset('counter');
