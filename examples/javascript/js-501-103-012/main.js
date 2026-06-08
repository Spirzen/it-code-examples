function formatDate(date, format = 'DD.MM.YYYY') {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    const hours = String(date.getHours()).padStart(2, '0');
    const minutes = String(date.getMinutes()).padStart(2, '0');
    const seconds = String(date.getSeconds()).padStart(2, '0');

    const map = {
        YYYY: year,
        MM: month,
        DD: day,
        HH: hours,
        mm: minutes,
        ss: seconds
    };

    let result = format;
    for (const key in map) {
        result = result.replace(key, map[key]);
    }
    return result;
}

function parseDate(dateString, format = 'DD.MM.YYYY') {
    const parts = format.match(/[DYM]+|[Hm]+|[Ss]+|[Aa]+/g);
    const values = dateString.split(/[-/.:/ ]+/);
    
    let year, month, day, hour, minute, second;

    // Простая логика сопоставления для формата DD.MM.YYYY
    if (format === 'DD.MM.YYYY') {
        day = parseInt(values[0], 10);
        month = parseInt(values[1], 10) - 1; // Месяцы с 0
        year = parseInt(values[2], 10);
    } else if (format === 'YYYY-MM-DD') {
        year = parseInt(values[0], 10);
        month = parseInt(values[1], 10) - 1;
        day = parseInt(values[2], 10);
    } else {
        throw new Error('Неподдерживаемый формат парсинга');
    }

    const date = new Date(year, month, day);
    
    if (isNaN(date.getTime())) {
        throw new Error('Некорректная дата');
    }

    return date;
}

// Пример использования
const now = new Date();
console.log('Стандартный формат:', formatDate(now, 'YYYY-MM-DD HH:mm:ss'));
console.log('Европейский формат:', formatDate(now, 'DD.MM.YYYY'));

const parsed = parseDate('06.05.2026', 'DD.MM.YYYY');
console.log('Распарсенная дата:', formatDate(parsed));
