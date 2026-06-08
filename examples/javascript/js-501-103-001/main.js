/**
 * Генератор безопасных паролей
 * @param {number} length - Длина пароля
 * @param {boolean} useDigits - Включать ли цифры
 * @param {boolean} useSymbols - Включать ли специальные символы
 * @returns {string} Сгенерированный пароль
 */
function generatePassword(length = 12, useDigits = true, useSymbols = true) {
    const lowercaseChars = 'abcdefghijklmnopqrstuvwxyz';
    const uppercaseChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const digitChars = '0123456789';
    const symbolChars = '!@#$%^&*()_+-=[]{}|;:,.<>?';

    let charPool = lowercaseChars + uppercaseChars;

    if (useDigits) {
        charPool += digitChars;
    }

    if (useSymbols) {
        charPool += symbolChars;
    }

    let password = '';
    
    // Гарантируем наличие хотя бы одного символа каждого типа при включении опций
    if (useDigits && length > 0) {
        password += digitChars[Math.floor(Math.random() * digitChars.length)];
        length--;
    }

    if (useSymbols && length > 0) {
        password += symbolChars[Math.floor(Math.random() * symbolChars.length)];
        length--;
    }

    // Заполняем оставшуюся длину случайными символами из общего пула
    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * charPool.length);
        password += charPool[randomIndex];
    }

    // Перемешиваем строку, чтобы гарантированный символ не всегда был первым
    return password.split('').sort(() => 0.5 - Math.random()).join('');
}

// Пример использования
const myPassword = generatePassword(16, true, true);
console.log(`Сгенерированный пароль: ${myPassword}`);
