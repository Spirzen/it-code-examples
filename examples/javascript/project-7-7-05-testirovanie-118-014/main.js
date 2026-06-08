it('должен заполнить форму и отправить запрос', async () => {
  await page.goto('https://example.com/form');
  
  // Заполнение полей
  await page.type('#username', 'Ivan');
  await page.type('#email', 'ivan@example.com');
  
  // Нажатие кнопки (с автоматическим ожиданием доступности)
  await page.click('button[type="submit"]');
  
  // Проверка результата (ожидание появления элемента)
  await page.waitForSelector('.success-message');
  
  const text = await page.$eval('.success-message', el => el.innerText);
  expect(text).toContain('Данные отправлены');
});
