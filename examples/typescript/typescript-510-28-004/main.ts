type Events = {
  CART_ITEM_ADDED: { productId: string; price: number };
  USER_AUTHENTICATED: { userId: string; role: "admin" | "customer" };
  PAYMENT_COMPLETED: { orderId: string; currency: "USD" | "EUR" };
};

class TypedEmitter {
  private handlers: {
    [K in keyof Events]?: Array<(payload: Events[K]) => void>;
  } = {};

  on<K extends keyof Events>(event: K, fn: (payload: Events[K]) => void): void {
    const list = this.handlers[event] ?? [];
    list.push(fn);
    this.handlers[event] = list;
  }

  emit<K extends keyof Events>(event: K, payload: Events[K]): void {
    for (const fn of this.handlers[event] ?? []) {
      fn(payload);
    }
  }
}

const bus = new TypedEmitter();

bus.emit("CART_ITEM_ADDED", { productId: "p_001", price: 49.99 });

// bus.emit("PAYMENT_COMPLETED", {
//   orderId: "o_456",
//   currency: "GBP",
// });
// ошибка: "GBP" не входит в "USD" | "EUR"

bus.on("PAYMENT_COMPLETED", ({ orderId, currency }) => {
  console.log(orderId, currency);
});

// bus.on("PAYMENT_COMPLETED", ({ userId }) => {
//   console.log(userId);
// });
// ошибка: userId есть у USER_AUTHENTICATED, не у PAYMENT_COMPLETED
