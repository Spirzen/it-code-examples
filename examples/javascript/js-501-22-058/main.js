class DatabaseConnection {
    constructor(connectionString) {
        this.connectionString = connectionString;
        this.connected = true;
        console.log(`Подключение к базе данных установлено`);
    }
    
    async query(sql) {
        return `Результат запроса: ${sql}`;
    }
    
    async [Symbol.asyncDispose]() {
        if (this.connected) {
            console.log(`Подключение к базе данных закрыто`);
            this.connected = false;
        }
    }
}

async function processData() {
    await using db = new DatabaseConnection("connection-string");
    const result = await db.query("SELECT * FROM users");
    console.log(result);
    // Подключение автоматически закроется при выходе из блока
}

await processData();
