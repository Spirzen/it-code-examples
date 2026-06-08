import { GameProvider, useGame } from './hooks/useGame';
import { MenuScreen } from './components/MenuScreen';
import { MapScreen } from './components/MapScreen';
import { CombatScreen } from './components/CombatScreen';
import { RewardScreen, ShopScreen, RestScreen, GameOverScreen } from './components/Screens';

function GameRouter() {
  const { run, tick } = useGame();
  void tick;

  const screens: Record<string, React.ReactNode> = {
    menu: <MenuScreen />,
    map: <MapScreen />,
    combat: <CombatScreen />,
    reward: <RewardScreen />,
    shop: <ShopScreen />,
    rest: <RestScreen />,
    game_over: <GameOverScreen victory={false} />,
    victory: <GameOverScreen victory={true} />,
  };

  return <div className="screen-wrap">{screens[run.screen] ?? null}</div>;
}
