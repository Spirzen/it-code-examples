const { test, expect } = require('@playwright/test');

test.describe('Демо-форма входа', () => {
  test('успешный вход показывает приветствие', async ({ page }) => {
    await page.goto('https://the-internet.herokuapp.com/login');

    await page.fill('#username', 'tomsmith');
    await page.fill('#password', 'SuperSecretPassword!');
    await page.click('button[type="submit"]');

    await expect(page.locator('#flash')).toContainText('You logged into');
  });

  test('неверный пароль показывает ошибку', async ({ page }) => {
    await page.goto('https://the-internet.herokuapp.com/login');

    await page.fill('#username', 'tomsmith');
    await page.fill('#password', 'wrong');
    await page.click('button[type="submit"]');

    await expect(page.locator('#flash')).toContainText('Your password is invalid');
  });
});
