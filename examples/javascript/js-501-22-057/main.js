// DisposableStack для синхронных ресурсов
class FileHandle {
    constructor(filename) {
        this.filename = filename;
        this.open = true;
        console.log(`Файл ${filename} открыт`);
    }
    
    read() {
        return `Содержимое файла ${this.filename}`;
    }
    
    [Symbol.dispose]() {
        if (this.open) {
            console.log(`Файл ${this.filename} закрыт`);
            this.open = false;
        }
    }
}

function processFile() {
    using file = new FileHandle("data.txt");
    console.log(file.read());
    // Файл автоматически закроется при выходе из блока
}

processFile();
