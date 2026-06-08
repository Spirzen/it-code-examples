const puppeteer = require('puppeteer');

describe('Тестирование главной страницы', () => {
  let browser;
  let page;

  // Инициализация перед каждым тестом
  beforeEach(async () => {
    browser = await puppeteer.launch({ headless: 'new' });
    page = await browser.newPage();
  });

  // Очистка после каждого теста
  afterEach(async () => {
    await browser.close();
  });

  it('должен загрузить заголовок', async () => {
    await page.goto('https://example.com');
    const title = await page.title();
    expect(title).toBe('Example Domain');
  });
});
