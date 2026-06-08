import { GameProvider, useGame } from './hooks/useGame';
import { MenuScreen } from './components/MenuScreen';

function GameRouter() {
  const { run, tick } = useGame();
  void tick;

  if (run.screen === 'menu') return <MenuScreen />;
  if (run.screen === 'map') return <div className="screen"><p>Карта — этап 10</p></div>;
  return null;
}

export default function App() {
  return (
    <GameProvider>
      <div className="app">
        <GameRouter />
      </div>
    </GameProvider>
  );
}
