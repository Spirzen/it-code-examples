type CartItem = { sku: string; qty: number };

type CartState = { items: CartItem[] };

type CartAction =
  | { type: "add"; sku: string }
  | { type: "remove"; sku: string }
  | { type: "clear" };

function cartReducer(state: CartState, action: CartAction): CartState {
  switch (action.type) {
    case "add":
      return {
        items: [...state.items, { sku: action.sku, qty: 1 }],
      };
    case "remove":
      return {
        items: state.items.filter((i) => i.sku !== action.sku),
      };
    case "clear":
      return { items: [] };
    default: {
      const _exhaustive: never = action;
      return _exhaustive;
    }
  }
}

function Cart() {
  const [state, dispatch] = React.useReducer(cartReducer, { items: [] });

  return (
    <button type="button" onClick={() => dispatch({ type: "add", sku: "book-1" })}>
      Добавить ({state.items.length})
    </button>
  );
}
