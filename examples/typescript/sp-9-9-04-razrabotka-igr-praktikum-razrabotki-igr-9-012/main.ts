import type { Screen } from './types';
import { Player } from './player';

export class RunState {
  screen: Screen = 'menu';
  player = new Player();

  goToMenu() {
    this.screen = 'menu';
  }

  startNewRun() {
    this.player = new Player();
    this.screen = 'map';
  }
}
