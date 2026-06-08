// components/HeaderComponent.ts

import { Page, Locator } from '@playwright/test';

export class HeaderComponent {
  readonly cartLink: Locator;

  constructor(private page: Page) {
    this.cartLink = page.getByTestId('header-cart');
  }

  async openCart() {
    await this.cartLink.click();
  }
}

// pages/CatalogPage.ts
export class CatalogPage {
  readonly header: HeaderComponent;

  constructor(page: Page) {
    this.header = new HeaderComponent(page);
  }
}
