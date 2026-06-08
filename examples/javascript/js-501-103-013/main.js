const { execSync } = require('child_process');
const os = require('os');

function getProcesses(filterName = '') {
    let command;
    let args;

    const platform = os.platform();

    if (platform === 'win32') {
        command = 'wmic';
        args = ['process', 'get', 'Name,PID,CPU,Memory'].join(' ');
    } else {
        // Linux / macOS
        command = 'ps';
        args = ['-ef'];
    }

    try {
        const output = execSync(`${command} ${args}`, { encoding: 'utf-8' });
        const lines = output.trim().split('\n');
        
        const processes = [];

        // Пропускаем заголовок (если есть)
        const startLine = platform === 'win32' ? 1 : 1; 

        for (let i = startLine; i < lines.length; i++) {
            const line = lines[i].trim();
            if (!line) continue;

            let processObj = {};

            if (platform === 'win32') {
                // Простой парсинг для wmic (может требовать доработки для сложных случаев)
                const parts = line.split(/\s+/);
                if (parts.length >= 2) {
                    processObj = {
                        name: parts[0],
                        pid: parts[1] || 'N/A',
                        cpu: parts[2] || 'N/A',
                        memory: parts[3] || 'N/A'
                    };
                }
            } else {
                // Парсинг для ps -ef (UID PID PPID C STIME TTY TIME CMD)
                const parts = line.split(/\s+/);
                if (parts.length >= 7) {
                    processObj = {
                        uid: parts[0],
                        pid: parts[1],
                        ppid: parts[2],
                        time: parts[6], // Время выполнения
                        cmd: parts.slice(7).join(' ') // Команда
                    };
                }
            }

            if (Object.keys(processObj).length > 0) {
                if (filterName && !processObj.name?.includes(filterName) && !processObj.cmd?.includes(filterName)) {
                    continue;
                }
                processes.push(processObj);
            }
        }

        return processes;

    } catch (error) {
        console.error('Ошибка выполнения команды:', error.message);
        return [];
    }
}

function displayProcesses(processes) {
    console.table(processes);
}

// Пример вызова
const allProcs = getProcesses();
displayProcesses(allProcs.slice(0, 10)); // Показать первые 10

const nodeProcs = getProcesses('node');
if (nodeProcs.length > 0) {
    console.log('\nНайдены процессы Node.js:');
    displayProcesses(nodeProcs);
}
