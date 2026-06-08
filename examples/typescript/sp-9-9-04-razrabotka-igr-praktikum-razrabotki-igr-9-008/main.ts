import {
  STARTING_HP,
  STARTING_ENERGY,
  STARTING_GOLD,
  MAX_ENERGY,
} from './settings';
import { Deck, Hand, createStartingDeck } from './card';
import type { Card } from './card';
import type { Relic } from './relic';

export class Player {
  maxHp = STARTING_HP;
  hp = STARTING_HP;
  energy = STARTING_ENERGY;
  maxEnergy = STARTING_ENERGY;
  gold = STARTING_GOLD;
  block = 0;
  strength = 0;
  vulnerable = 0;
  weak = 0;
  deck: Deck;
  hand: Hand;
  relics: Relic[] = [];

  constructor() {
    this.deck = new Deck(createStartingDeck());
    this.hand = new Hand();
  }

  resetCombat() {
    this.energy = this.maxEnergy;
    this.block = 0;
    this.vulnerable = 0;
    this.weak = 0;
    this.hand.clear();
    const all = this.deck.getAllCards();
    this.deck = new Deck(all);
  }

  startTurn() {
    this.energy = this.maxEnergy;
    this.block = 0;
    if (this.vulnerable > 0) this.vulnerable--;
    if (this.weak > 0) this.weak--;
  }

  endTurn() {
    const cards = [...this.hand.cards];
    this.hand.clear();
    this.deck.discardAll(cards);
  }

  gainBlock(amount: number) {
    this.block += amount;
  }

  takeDamage(amount: number): number {
    if (this.vulnerable > 0) amount = Math.floor(amount * 1.5);
    const blocked = Math.min(this.block, amount);
    this.block -= blocked;
    const damage = amount - blocked;
    this.hp = Math.max(0, this.hp - damage);
    return damage;
  }

  heal(amount: number) {
    this.hp = Math.min(this.maxHp, this.hp + amount);
  }

  spendEnergy(cost: number): boolean {
    if (this.energy >= cost) {
      this.energy -= cost;
      return true;
    }
    return false;
  }

  gainEnergy(amount: number) {
    this.energy = Math.min(MAX_ENERGY, this.energy + amount);
  }

  getAttackDamage(base: number): number {
    let damage = base + this.strength;
    if (this.weak > 0) damage = Math.floor(damage * 0.75);
    return Math.max(0, damage);
  }

  isAlive() {
    return this.hp > 0;
  }

  addCardToDeck(card: Card) {
    this.deck.drawPile.push(card.copy());
  }
}
