export type CardType =
  | 'attack'
  | 'block'
  | 'buff'
  | 'debuff'
  | 'draw'
  | 'creature';

export type CardRarity = 'basic' | 'common' | 'uncommon' | 'rare' | 'custom';

export interface CardData {
  id: string;
  name: string;
  type: CardType;
  cost: number;
  value: number;
  description: string;
  rarity: CardRarity;
  effect?: string;
  effect_value?: number;
  aoe?: boolean;
  block?: number;
  draw?: number;
}

export type Screen =
  | 'menu'
  | 'map'
  | 'combat'
  | 'reward'
  | 'shop'
  | 'rest'
  | 'game_over'
  | 'victory';
