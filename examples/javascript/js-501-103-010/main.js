const os = require('os');

function checkDiskSpace() {
    const platforms = ['linux', 'darwin']; // Linux и macOS
    const platform = os.platform();

    if (!platforms.includes(platform)) {
        console.log('Модуль os.diskSpace работает некорректно на этой платформе (Windows).');
        console.log('Для Windows требуется использование child_process.execSync.');
        return;
    }

    const diskInfo = os.freemem();
    const totalMem = os.totalmem();
    const percentFree = ((diskInfo / totalMem) * 100).toFixed(2);

    console.log(`\n=== Статус памяти ===`);
    console.log(`Всего памяти: ${(totalMem / 1024 / 1024 / 1024).toFixed(2)} GB`);
    console.log(`Свободно памяти: ${(diskInfo / 1024 / 1024 / 1024).toFixed(2)} GB`);
    console.log(`Занято памяти: ${percentFree}% свободно`);

    // Проверка дисков (Linux/macOS)
    const mounts = os.mountinfo(); // Доступно в некоторых версиях Node.js, иначе через fs
    
    // Альтернативный способ через child_process для точности
    const { execSync } = require('child_process');
    try {
        const dfOutput = execSync('df -h').toString();
        console.log('\n=== Статус дисков ===');
        console.log(dfOutput);
    } catch (e) {
        console.log('Не удалось получить информацию о дисках через команду df.');
    }
}

checkDiskSpace();
