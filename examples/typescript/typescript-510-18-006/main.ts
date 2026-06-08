interface CartState {
  items: { sku: string; qty: number }[];
}

function addItem(state: CartState, sku: string): CartState {
  const existing = state.items.find((i) => i.sku === sku);
  if (existing) {
    return {
      items: state.items.map((i) =>
        i.sku === sku ? { ...i, qty: i.qty + 1 } : i,
      ),
    };
  }
  return { items: [...state.items, { sku, qty: 1 }] };
}
