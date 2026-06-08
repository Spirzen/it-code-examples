const fs = require('fs').promises;
const path = require('path');

async function scanDirectory(dirPath, extensions = []) {
    let files = [];
    let directories = [];
    let totalSize = 0;

    try {
        const items = await fs.readdir(dirPath, { withFileTypes: true });

        for (const item of items) {
            const fullPath = path.join(dirPath, item.name);

            if (item.isDirectory()) {
                directories.push(item.name);
                const subFiles = await scanDirectory(fullPath, extensions);
                files = files.concat(subFiles.files);
                totalSize += subFiles.totalSize;
            } else {
                if (extensions.length === 0 || extensions.includes(path.extname(item.name))) {
                    const stats = await fs.stat(fullPath);
                    files.push({ name: item.name, path: fullPath, size: stats.size });
                    totalSize += stats.size;
                }
            }
        }
    } catch (error) {
        console.error(`Ошибка доступа к директории ${dirPath}:`, error.message);
    }

    return { files, directories, totalSize };
}

async function main() {
    const results = await scanDirectory('./docs', ['.txt', '.md']);
    
    console.log(`Найдено файлов: ${results.files.length}`);
    console.log(`Найдено папок: ${results.directories.length}`);
    console.log(`Общий размер: ${(results.totalSize / 1024).toFixed(2)} KB`);
    
    console.log('\nСписок файлов:');
    results.files.forEach(f => console.log(`- ${f.name} (${f.size} байт)`));
}

// main();
