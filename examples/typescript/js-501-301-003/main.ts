type Action =
  | { type: 'add'; amount: number }
  | { type: 'clear' };

function apply(state: number, action: Action): number {
  switch (action.type) {
    case 'add': return state + action.amount;
    case 'clear': return 0;
    default: {
      const _check: never = action;
      return _check;
    }
  }
}
