import { useGame } from '../hooks/useGame';
import { NODE_ICONS, NODE_COLORS } from '../game/settings';

export function MapScreen() {
  const { run, dispatch } = useGame();
  const map = run.gameMap;
  if (!map) return null;

  return (
    <div className="screen map-screen">
      <h2>Шпиль — этаж {map.getFloorProgress()[0] + 1} / {map.getFloorProgress()[1]}</h2>
      <div className="map-grid">
        {map.floors.map((floor, fi) => (
          <div key={fi} className="map-floor">
            {floor.map((node, ni) => (
              <button
                key={ni}
                type="button"
                className={`map-node ${node.available ? 'map-node--available' : ''} ${node.completed ? 'map-node--done' : ''}`}
                style={{ borderColor: NODE_COLORS[node.type] }}
                disabled={!node.available}
                onClick={() => dispatch({ type: 'SELECT_NODE', node })}
              >
                {NODE_ICONS[node.type] ?? '?'}
              </button>
            ))}
          </div>
        ))}
      </div>
      <p>Золото: {run.player.gold} · HP: {run.player.hp}/{run.player.maxHp}</p>
    </div>
  );
}
