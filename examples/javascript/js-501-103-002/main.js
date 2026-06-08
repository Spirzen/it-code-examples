const fs = require('fs').promises;

async function sortTextFile(inputPath, outputPath) {
    try {
        // Чтение содержимого файла
        const data = await fs.readFile(inputPath, 'utf-8');
        
        // Разбиение текста на строки и фильтрация пустых строк
        const lines = data.split('\n')
                          .map(line => line.trim())
                          .filter(line => line.length > 0);

        // Сортировка строк в алфавитном порядке
        const sortedLines = lines.sort((a, b) => a.localeCompare(b));

        // Объединение отсортированных строк обратно в текст
        const result = sortedLines.join('\n');

        // Запись результата в новый файл
        await fs.writeFile(outputPath, result, 'utf-8');
        
        console.log(`Успешно обработано строк: ${sortedLines.length}`);
        console.log(`Результат сохранен в: ${outputPath}`);
    } catch (error) {
        console.error('Ошибка при обработке файла:', error.message);
    }
}

// Пример вызова
// sortTextFile('input.txt', 'output_sorted.txt');
