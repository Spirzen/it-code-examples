const fs = require('fs').promises;
const path = require('path');
const { execSync } = require('child_process');

async function createBackup(sourcePath, backupDir) {
    try {
        // Проверка существования источника
        await fs.access(sourcePath);
        
        // Создание директории бэкапа, если её нет
        await fs.mkdir(backupDir, { recursive: true });

        const fileName = path.basename(sourcePath);
        const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
        const backupFileName = `${timestamp}_${fileName}`;
        const backupPath = path.join(backupDir, backupFileName);

        // Копирование файла
        await fs.copyFile(sourcePath, backupPath);
        
        console.log(`Бэкап создан: ${backupPath}`);
        
        // Опционально: удаление старых бэкапов (например, старше 7 дней)
        // Логика удаления требует дополнительного цикла по файлам в backupDir
        
    } catch (error) {
        console.error('Ошибка создания бэкапа:', error.message);
    }
}

// Пример вызова
// createBackup('./important_file.txt', './backups');
