import relicsData from '../data/relics.json';
import type { Player } from './player';
import type { Enemy } from './enemy';

export class Relic {
  id: string;
  name: string;
  description: string;
  effect: string;
  value: number;

  constructor(data: (typeof relicsData)[0]) {
    this.id = data.id;
    this.name = data.name;
    this.description = data.description;
    this.effect = data.effect;
    this.value = data.value;
  }
}

export function getRelicPickOptions(count: number): Relic[] {
  const shuffled = [...relicsData].sort(() => Math.random() - 0.5);
  return shuffled.slice(0, count).map((d) => new Relic(d));
}

export function applyRelicOnCombatStart(player: Player, relic: Relic, enemies: Enemy[]) {
  if (relic.effect === 'start_vulnerable') {
    for (const e of enemies) e.applyVulnerable(relic.value);
  }
}

export function applyRelicOnCombatEnd(player: Player, relic: Relic) {
  if (relic.effect === 'heal_after_combat') {
    player.heal(relic.value);
  }
}
