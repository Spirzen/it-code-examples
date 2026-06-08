window.addEventListener('error', function(event) {
    console.error('Глобальная ошибка:', event.message);
    console.error('Файл:', event.filename);
    console.error('Строка:', event.lineno);
    console.error('Столбец:', event.colno);
    console.error('Ошибка:', event.error);
    
    // Предотвращение стандартного обработчика
    event.preventDefault();
});

window.addEventListener('unhandledrejection', function(event) {
    console.error('Необработанное промис-исключение:', event.reason);
    event.preventDefault();
});
