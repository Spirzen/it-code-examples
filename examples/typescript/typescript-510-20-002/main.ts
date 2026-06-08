type OrderCreatedDetail = { orderId: string };

const event = new CustomEvent<OrderCreatedDetail>("order:created", {
  detail: { orderId: "ord-1" },
  bubbles: true,
});

window.addEventListener("order:created", (e: Event) => {
  if (!(e instanceof CustomEvent)) return;
  const detail = e.detail as OrderCreatedDetail;
  console.log(detail.orderId);
});

window.dispatchEvent(event);
