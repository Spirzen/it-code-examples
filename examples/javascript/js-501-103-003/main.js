function calculate(num1, num2, operator) {
    switch (operator) {
        case '+':
            return num1 + num2;
        case '-':
            return num1 - num2;
        case '*':
            return num1 * num2;
        case '/':
            if (num2 === 0) {
                throw new Error('Деление на ноль невозможно');
            }
            return num1 / num2;
        default:
            throw new Error(`Неизвестный оператор: ${operator}`);
    }
}

async function runCalculator() {
    const readline = require('readline').createInterface({
        input: process.stdin,
        output: process.stdout
    });

    const question = (query) => new Promise(resolve => readline.question(query, resolve));

    while (true) {
        console.log('\n=== Калькулятор ===');
        console.log('Доступные операции: +, -, *, /');
        console.log('Введите "exit" для завершения');

        const num1Str = await question('Первое число: ');
        if (num1Str.toLowerCase() === 'exit') break;

        const num2Str = await question('Второе число: ');
        const operator = await question('Оператор (+, -, *, /): ');

        const num1 = parseFloat(num1Str);
        const num2 = parseFloat(num2Str);

        if (isNaN(num1) || isNaN(num2)) {
            console.log('Ошибка: Введены некорректные числа.');
            continue;
        }

        try {
            const result = calculate(num1, num2, operator);
            console.log(`Результат: ${result}`);
        } catch (err) {
            console.log(`Ошибка: ${err.message}`);
        }
    }

    readline.close();
    console.log('Программа завершена.');
}

// Для запуска используйте: runCalculator();
