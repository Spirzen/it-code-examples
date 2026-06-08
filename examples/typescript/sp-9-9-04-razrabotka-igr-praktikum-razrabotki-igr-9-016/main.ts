case 'PLAY_CARD': {
  const combat = run.combat;
  if (!combat || combat.combatOver) break;
  const card = combat.player.hand.cards[action.cardIndex];
  if (!combat.canPlayCard(action.cardIndex)) break;
  if (combat.cardNeedsTarget(card)) {
    const target = combat.resolveTargetIndex(card, action.targetIndex);
    if (target === null) {
      combat.selectedCardIndex = action.cardIndex;
      break;
    }
  }
  combat.selectedCardIndex = null;
  combat.selectedEnemyIndex = null;
  combat.playCard(action.cardIndex, action.targetIndex);
  // sfx + проверка combatOver → onCombatVictory / onCombatDefeat
  break;
}
