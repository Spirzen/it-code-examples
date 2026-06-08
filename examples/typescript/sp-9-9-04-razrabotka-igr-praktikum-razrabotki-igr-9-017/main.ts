import type { Card } from '../game/card';
import { CARD_TYPE_COLORS } from '../game/settings';

interface Props {
  card: Card;
  playable: boolean;
  selected?: boolean;
  onClick?: () => void;
}

export function CardView({ card, playable, selected, onClick }: Props) {
  const border = CARD_TYPE_COLORS[card.type] ?? '#666';
  return (
    <button
      type="button"
      className={`card-view ${playable ? 'card-view--playable' : ''} ${selected ? 'card-view--selected' : ''}`}
      style={{ borderColor: border }}
      onClick={onClick}
      disabled={!playable && !onClick}
    >
      <span className="card-view__cost">{card.cost}</span>
      <span className="card-view__name">{card.name}</span>
      <span className="card-view__desc">{card.description}</span>
      <span className="card-view__value">{card.value}</span>
    </button>
  );
}
