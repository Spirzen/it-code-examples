import { useGame } from '../hooks/useGame';

export function MenuScreen() {
  const { dispatch } = useGame();

  return (
    <div className="screen menu-screen">
      <h1 className="title-display">Приключения Урала Батыра</h1>
      <p className="subtitle">Карточный roguelike — этап 7</p>
      <div className="menu-buttons">
        <button className="btn btn--gold" onClick={() => dispatch({ type: 'BEGIN_RUN' })}>
          Новый забег
        </button>
      </div>
    </div>
  );
}
