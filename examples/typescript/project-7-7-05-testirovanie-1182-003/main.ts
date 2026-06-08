// pages/PageFactory.ts

import { Page } from '@playwright/test';
import { LoginPage } from './LoginPage';
import { CatalogPage } from './CatalogPage';

export class PageFactory {
  constructor(private page: Page) {}

  loginPage() {
    return new LoginPage(this.page);
  }

  catalogPage() {
    return new CatalogPage(this.page);
  }
}

// tests/checkout.spec.ts
test('оформление заказа', async ({ page }) => {
  const pages = new PageFactory(page);
  await pages.loginPage().login('qa@test.local', 'Secret123!');
  await pages.catalogPage().addFirstItemToCart();
});
