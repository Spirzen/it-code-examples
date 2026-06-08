import { describe, it, expect } from 'vitest';
import { upgradeCard } from './upgrade';
import { Card } from './card';
import { Player } from './player';
import { SeededRNG } from './rng';

describe('upgradeCard', () => {
  it('buffs attack value', () => {
    const c = new Card({
      id: 'strike', name: 'Удар', type: 'attack', cost: 1, value: 6,
      description: '', rarity: 'basic',
    });
    expect(upgradeCard(c).value).toBe(9);
  });
});

describe('Player damage', () => {
  it('applies vulnerable multiplier', () => {
    const p = new Player();
    p.hp = 50;
    p.vulnerable = 2;
    p.takeDamage(10);
    expect(p.hp).toBe(35);
  });
});
