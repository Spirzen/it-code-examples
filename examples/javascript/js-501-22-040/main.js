// Используется при обработке ошибок с подавлением
try {
    try {
        throw new Error("Первичная ошибка");
    } catch (primaryError) {
        try {
            // Код очистки, который тоже может выбросить ошибку
            throw new Error("Ошибка очистки");
        } catch (cleanupError) {
            // Подавляем ошибку очистки
            throw new SuppressedError(cleanupError, primaryError, "Ошибка при очистке");
        }
    }
} catch (error) {
    console.log(error.name); // "SuppressedError"
    console.log(error.error); // Ошибка очистки
    console.log(error.suppressed); // Первичная ошибка
}
