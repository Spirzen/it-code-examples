import cardsData from '../data/cards.json';
import type { CardData } from './types';

const cardDb = cardsData as CardData[];

export class Card {
  id: string;
  name: string;
  type: string;
  cost: number;
  value: number;
  description: string;
  rarity: string;
  effect?: string;
  effect_value: number;

  constructor(data: CardData) {
    this.id = data.id;
    this.name = data.name;
    this.type = data.type;
    this.cost = data.cost;
    this.value = data.value ?? 0;
    this.description = data.description ?? '';
    this.rarity = data.rarity ?? 'common';
    this.effect = data.effect;
    this.effect_value = data.effect_value ?? 0;
  }

  copy(): Card {
    return new Card({
      id: this.id,
      name: this.name,
      type: this.type as CardData['type'],
      cost: this.cost,
      value: this.value,
      description: this.description,
      rarity: this.rarity as CardData['rarity'],
      effect: this.effect,
      effect_value: this.effect_value,
    });
  }
}

export function createCard(data: CardData): Card {
  return new Card({ ...data });
}

export function getCardById(id: string): CardData | undefined {
  return cardDb.find((c) => c.id === id);
}

export function createStartingDeck(): Card[] {
  const strike = getCardById('strike')!;
  const defend = getCardById('defend')!;
  const deck: Card[] = [];
  for (let i = 0; i < 5; i++) deck.push(createCard(strike));
  for (let i = 0; i < 5; i++) deck.push(createCard(defend));
  return deck;
}
