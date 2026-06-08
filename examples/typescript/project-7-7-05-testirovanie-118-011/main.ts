
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests', // Директория с тестами
  fullyParallel: true, // Параллельный запуск тестов
  forbidOnly: !!process.env.CI, // Запрет дубликатов в CI
  retries: process.env.CI ? 2 : 0, // Количество повторов при ошибке в CI
  workers: process.env.CI ? 1 : undefined,
  reporter: 'html', // Генерация HTML-отчета
  use: {
    baseURL: 'https://example.com', // Базовый URL
    trace: 'on-first-retry', // Запись трассировки при первой ошибке
    screenshot: 'only-on-failure', // Скриншоты только при падении
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },
  ],
});
