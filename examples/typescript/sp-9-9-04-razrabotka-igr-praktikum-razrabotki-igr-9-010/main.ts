import enemiesData from '../data/enemies.json';
import type { EnemyData } from './types';
import type { Player } from './player';

export const INTENT_ATTACK = 'attack';
export const INTENT_BLOCK = 'block';
export const INTENT_BUFF = 'buff';
export const INTENT_DEBUFF = 'debuff';
export const INTENT_UNKNOWN = 'unknown';

const enemyDb = enemiesData as Record<string, EnemyData>;

export class Enemy {
  id: string;
  name: string;
  maxHp: number;
  hp: number;
  block = 0;
  strength = 0;
  vulnerable = 0;
  weak = 0;
  intentPattern: string[];
  attackDamage: number;
  blockValue: number;
  buffValue: number;
  debuffValue: number;
  intentIndex = 0;
  currentIntent = INTENT_UNKNOWN;
  intentValue = 0;
  alive = true;

  constructor(data: EnemyData & { id?: string }, hpMult = 1) {
    this.id = data.id ?? 'unknown';
    this.name = data.name;
    this.maxHp = Math.floor(data.hp * hpMult);
    this.hp = this.maxHp;
    this.intentPattern = data.intent_pattern;
    this.attackDamage = data.attack_damage ?? 6;
    this.blockValue = data.block_value ?? 5;
    this.buffValue = data.buff_value ?? 2;
    this.debuffValue = data.debuff_value ?? 1;
    this.planIntent();
  }

  planIntent() {
    const intent = this.intentPattern[this.intentIndex % this.intentPattern.length];
    this.intentIndex++;
    this.currentIntent = intent;
    switch (intent) {
      case INTENT_ATTACK:
        this.intentValue = this.calcDamage(this.attackDamage);
        break;
      case INTENT_BLOCK:
        this.intentValue = this.blockValue;
        break;
      case INTENT_BUFF:
        this.intentValue = this.buffValue;
        break;
      case INTENT_DEBUFF:
        this.intentValue = this.debuffValue;
        break;
      default:
        this.intentValue = 0;
    }
  }

  calcDamage(base: number): number {
    let damage = base + this.strength;
    if (this.weak > 0) damage = Math.floor(damage * 0.75);
    return Math.max(0, damage);
  }

  takeDamage(amount: number): number {
    if (this.vulnerable > 0) amount = Math.floor(amount * 1.5);
    const blocked = Math.min(this.block, amount);
    this.block -= blocked;
    const damage = amount - blocked;
    this.hp = Math.max(0, this.hp - damage);
    if (this.hp <= 0) this.alive = false;
    return damage;
  }

  applyVulnerable(turns: number) {
    this.vulnerable = Math.max(this.vulnerable, turns);
  }

  executeIntent(player: Player): string[] {
    const messages: string[] = [];
    switch (this.currentIntent) {
      case INTENT_ATTACK:
        player.takeDamage(this.intentValue);
        messages.push(`${this.name} наносит ${this.intentValue} урона`);
        break;
      case INTENT_BLOCK:
        this.block += this.intentValue;
        messages.push(`${this.name} получает ${this.intentValue} брони`);
        break;
      case INTENT_BUFF:
        this.strength += this.intentValue;
        messages.push(`${this.name} получает +${this.intentValue} силы`);
        break;
      case INTENT_DEBUFF:
        player.vulnerable = Math.max(player.vulnerable, this.intentValue);
        messages.push(`${this.name} накладывает Уязвимость (${this.intentValue})`);
        break;
    }
    this.planIntent();
    return messages;
  }
}

export class Encounter {
  enemies: Enemy[];

  constructor(enemies: Enemy[]) {
    this.enemies = enemies;
  }

  getLivingEnemies(): Enemy[] {
    return this.enemies.filter((e) => e.alive);
  }

  allDead(): boolean {
    return this.getLivingEnemies().length === 0;
  }
}

export function createCombatEncounter(isElite = false, isBoss = false): Encounter {
  const keys = Object.keys(enemyDb);
  const id = keys[Math.floor(Math.random() * keys.length)];
  const mult = isBoss ? 2.5 : isElite ? 1.6 : 1;
  const enemy = new Enemy({ ...enemyDb[id], id }, mult);
  return new Encounter([enemy]);
}
