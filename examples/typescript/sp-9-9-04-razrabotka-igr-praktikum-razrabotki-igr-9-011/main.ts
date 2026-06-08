import {
  CARD_ATTACK,
  CARD_BLOCK,
  CARD_DEBUFF,
  STARTING_HAND,
  DRAW_PER_TURN,
} from './settings';
import type { Player } from './player';
import type { Encounter } from './enemy';
import type { Card } from './card';

export class CombatManager {
  static STATE_PLAYER_TURN = 'player_turn';
  static STATE_ENEMY_TURN = 'enemy_turn';
  static STATE_VICTORY = 'victory';
  static STATE_DEFEAT = 'defeat';

  player: Player;
  encounter: Encounter;
  state = CombatManager.STATE_PLAYER_TURN;
  turn = 0;
  log: string[] = [];
  combatOver = false;
  victory = false;
  goldReward = 0;

  constructor(player: Player, encounter: Encounter) {
    this.player = player;
    this.encounter = encounter;
    this.initCombat();
  }

  initCombat() {
    this.player.resetCombat();
    const drawn = this.player.deck.draw(STARTING_HAND);
    for (const card of drawn) this.player.hand.add(card);
    this.turn = 1;
    this.log = [`Ход ${this.turn}. Ваш ход.`];
  }

  canPlayCard(cardIndex: number): boolean {
    if (this.state !== CombatManager.STATE_PLAYER_TURN) return false;
    const card = this.player.hand.cards[cardIndex];
    if (!card) return false;
    return this.player.energy >= card.cost;
  }

  cardNeedsTarget(card: Card): boolean {
    return card.type === CARD_ATTACK || card.type === CARD_DEBUFF;
  }

  playCard(cardIndex: number, targetEnemyIndex: number | null = null): boolean {
    if (!this.canPlayCard(cardIndex)) return false;
    const card = this.player.hand.cards[cardIndex];
    if (this.cardNeedsTarget(card)) {
      const living = this.encounter.getLivingEnemies();
      if (!living.length) return false;
      if (targetEnemyIndex === null && living.length > 1) return false;
      targetEnemyIndex = targetEnemyIndex ?? 0;
    }
    if (!this.player.spendEnergy(card.cost)) return false;

    const played = this.player.hand.remove(cardIndex)!;
    this.resolveCard(played, targetEnemyIndex);
    this.player.deck.addToDiscard(played);

    if (this.encounter.allDead()) this.endCombatVictory();
    return true;
  }

  resolveCard(card: Card, targetIndex: number | null) {
    const living = this.encounter.getLivingEnemies();
    if (card.type === CARD_ATTACK && living.length) {
      const enemy = living[targetIndex ?? 0];
      const dmg = this.player.getAttackDamage(card.value);
      enemy.takeDamage(dmg);
      this.addLog(`${card.name}: ${dmg} урона → ${enemy.name}`);
      if (card.effect === 'vulnerable') {
        enemy.applyVulnerable(card.effect_value);
      }
    } else if (card.type === CARD_BLOCK) {
      this.player.gainBlock(card.value);
      this.addLog(`${card.name}: +${card.value} брони`);
    }
  }

  endPlayerTurn() {
    if (this.state !== CombatManager.STATE_PLAYER_TURN) return;
    this.player.endTurn();
    this.state = CombatManager.STATE_ENEMY_TURN;
    this.enemyPhase();
    if (this.combatOver) return;
    this.startNextTurn();
  }

  enemyPhase() {
    for (const enemy of this.encounter.getLivingEnemies()) {
      for (const msg of enemy.executeIntent(this.player)) {
        this.addLog(msg);
      }
      if (!this.player.isAlive()) {
        this.endCombatDefeat();
        return;
      }
    }
  }

  startNextTurn() {
    this.turn++;
    this.player.startTurn();
    const drawn = this.player.deck.draw(DRAW_PER_TURN);
    for (const card of drawn) this.player.hand.add(card);
    this.state = CombatManager.STATE_PLAYER_TURN;
    this.addLog(`Ход ${this.turn}. Ваш ход.`);
  }

  endCombatVictory() {
    this.combatOver = true;
    this.victory = true;
    this.state = CombatManager.STATE_VICTORY;
    this.goldReward = 15;
    this.addLog('Победа!');
  }

  endCombatDefeat() {
    this.combatOver = true;
    this.victory = false;
    this.state = CombatManager.STATE_DEFEAT;
    this.addLog('Поражение…');
  }

  addLog(msg: string) {
    this.log.push(msg);
    if (this.log.length > 8) this.log = this.log.slice(-8);
  }
}
