import {
  createContext,
  useContext,
  useCallback,
  useRef,
  useState,
  type ReactNode,
} from 'react';
import { RunState } from '../game/runState';

type GameAction =
  | { type: 'GO_MENU' }
  | { type: 'BEGIN_RUN' };

interface GameContextValue {
  run: RunState;
  tick: number;
  dispatch: (action: GameAction) => void;
}

const GameContext = createContext<GameContextValue | null>(null);

function applyAction(run: RunState, action: GameAction) {
  switch (action.type) {
    case 'GO_MENU':
      run.goToMenu();
      break;
    case 'BEGIN_RUN':
      run.startNewRun();
      break;
  }
}

export function GameProvider({ children }: { children: ReactNode }) {
  const runRef = useRef(new RunState());
  const [tick, setTick] = useState(0);

  const dispatch = useCallback((action: GameAction) => {
    applyAction(runRef.current, action);
    setTick((t) => t + 1);
  }, []);

  return (
    <GameContext.Provider value={{ run: runRef.current, tick, dispatch }}>
      {children}
    </GameContext.Provider>
  );
}

export function useGame() {
  const ctx = useContext(GameContext);
  if (!ctx) throw new Error('useGame вне GameProvider');
  return ctx;
}
