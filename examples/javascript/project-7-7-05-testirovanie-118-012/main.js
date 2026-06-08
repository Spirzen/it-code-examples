const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    baseUrl: "https://example.com", // Базовый URL приложения
    setupNodeEvents(on, config) {
      // Здесь можно добавить плагины или хуки
      return config;
    },
    specPattern: 'cypress/e2e/**/*.cy.{js,jsx,ts,tsx}', // Шаблоны имен файлов тестов
    supportFile: 'cypress/support/e2e.js', // Файл глобальных настроек
    viewportWidth: 1920,
    viewportHeight: 1080,
    video: true, // Запись видео выполнения
    screenshotOnRunFailure: true, // Скриншот при ошибке
  },
});
