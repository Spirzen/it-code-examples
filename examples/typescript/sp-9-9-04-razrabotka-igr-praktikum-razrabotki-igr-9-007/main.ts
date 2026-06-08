import { MAX_HAND } from './settings';

export class Deck {
  drawPile: Card[] = [];
  discardPile: Card[] = [];

  constructor(cards: Card[] = []) {
    this.drawPile = [...cards];
    this.shuffle();
  }

  shuffle() {
    for (let i = this.drawPile.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [this.drawPile[i], this.drawPile[j]] = [this.drawPile[j], this.drawPile[i]];
    }
  }

  draw(count = 1): Card[] {
    const drawn: Card[] = [];
    for (let i = 0; i < count; i++) {
      if (this.drawPile.length === 0 && this.discardPile.length > 0) {
        this.drawPile = [...this.discardPile];
        this.discardPile = [];
        this.shuffle();
      }
      if (this.drawPile.length > 0) {
        drawn.push(this.drawPile.pop()!);
      }
    }
    return drawn;
  }

  addToDiscard(card: Card) {
    this.discardPile.push(card);
  }

  discardAll(cards: Card[]) {
    this.discardPile.push(...cards);
  }

  getAllCards(): Card[] {
    return [...this.drawPile, ...this.discardPile];
  }
}

export class Hand {
  cards: Card[] = [];
  maxSize: number;

  constructor(maxSize = MAX_HAND) {
    this.maxSize = maxSize;
  }

  add(card: Card): boolean {
    if (this.cards.length >= this.maxSize) return false;
    this.cards.push(card);
    return true;
  }

  remove(index: number): Card | null {
    if (index < 0 || index >= this.cards.length) return null;
    return this.cards.splice(index, 1)[0];
  }

  clear() {
    this.cards = [];
  }
}
