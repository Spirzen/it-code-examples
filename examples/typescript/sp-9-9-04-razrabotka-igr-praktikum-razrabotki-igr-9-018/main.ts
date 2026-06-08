import { useGame } from '../hooks/useGame';
import { CardView } from './CardView';

export function CombatScreen() {
  const { run, dispatch, tick } = useGame();
  void tick;
  const combat = run.combat;
  if (!combat) return null;

  return (
    <div className="screen combat-area">
      <div className="combat-hud">
        HP {combat.player.hp}/{combat.player.maxHp} · ⚡ {combat.player.energy} · 🛡 {combat.player.block}
      </div>

      <div className="enemy-row">
        {combat.encounter.getLivingEnemies().map((e, i) => (
          <button
            key={e.id + i}
            type="button"
            className="enemy-panel"
            onClick={() => dispatch({ type: 'SELECT_ENEMY', index: i })}
          >
            <div>{e.name}</div>
            <div>{e.hp}/{e.maxHp} HP</div>
            <div>Намерение: {e.currentIntent} ({e.intentValue})</div>
          </button>
        ))}
      </div>

      <div className="combat-log">
        {combat.log.map((line, i) => (
          <div key={i}>{line}</div>
        ))}
      </div>

      <div className="hand-row">
        {combat.player.hand.cards.map((card, i) => (
          <CardView
            key={`${card.id}-${i}`}
            card={card}
            playable={combat.canPlayCard(i)}
            selected={combat.selectedCardIndex === i}
            onClick={() => dispatch({ type: 'PLAY_CARD', cardIndex: i, targetIndex: combat.selectedEnemyIndex })}
          />
        ))}
      </div>

      <button
        type="button"
        className="btn btn--gold"
        onClick={() => dispatch({ type: 'END_TURN' })}
        disabled={combat.combatOver}
      >
        Конец хода (E)
      </button>
    </div>
  );
}
