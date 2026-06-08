// Плохо: метод на 100+ строк
public void generateReport() {
    // Подготовка данных
    // Форматирование
    // Валидация
    // Сохранение
    // Отправка
    // Логирование
    // ...
}

// Хорошо: декомпозиция
public void generateReport() {
    ReportData reportData = prepareReportData();
    String content = formatReport(reportData);
    validateReport(content);
    saveReport(content);
    sendReportNotification();
    logReportGeneration();
}
