class Config {
    static DEFAULT_TIMEOUT;
    static MAX_RETRIES;
    static API_URL;
    
    static {
        try {
            const env = process.env.NODE_ENV || 'Разработка';
            
            if (env === 'production') {
                this.DEFAULT_TIMEOUT = 30000;
                this.MAX_RETRIES = 3;
                this.API_URL = 'https://api.example.com';
            } else {
                this.DEFAULT_TIMEOUT = 5000;
                this.MAX_RETRIES = 1;
                this.API_URL = 'https://dev-api.example.com';
            }
            
            console.log('Конфигурация загружена');
        } catch (error) {
            console.error('Ошибка инициализации конфигурации:', error);
            this.DEFAULT_TIMEOUT = 10000;
            this.MAX_RETRIES = 2;
            this.API_URL = 'https://fallback-api.example.com';
        }
    }
}

console.log(Config.API_URL);
