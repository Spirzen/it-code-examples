import { NODE_COMBAT, NODE_ELITE, NODE_BOSS } from './settings';
import { getRewardCards } from './card';

enterNode(node: MapNode) {
  if ([NODE_COMBAT, NODE_ELITE, NODE_BOSS].includes(node.type)) {
    const isElite = node.type === NODE_ELITE;
    const isBoss = node.type === NODE_BOSS;
    this.combat = new CombatManager(
      this.player,
      createCombatEncounter(isElite, isBoss),
    );
    this.screen = 'combat';
  } else if (node.type === NODE_REST) {
    this.screen = 'rest';
  } else if (node.type === NODE_SHOP) {
    this.shopCards = getRewardCards(5);
    this.screen = 'shop';
  }
}

onCombatVictory() {
  this.rewardCards = getRewardCards(3);
  this.player.gold += this.combat?.goldReward ?? 0;
  this.screen = 'reward';
}

pickReward(index: number) {
  if (index >= 0 && index < this.rewardCards.length) {
    this.player.addCardToDeck(this.rewardCards[index]);
  }
  this.rewardCards = [];
  this.gameMap?.completeCurrentNode();
  this.combat = null;
  this.screen = 'map';
}
