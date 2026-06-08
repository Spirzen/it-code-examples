type PayloadMap = {
  "payment.succeeded": { chargeId: string; amount: number };
  "payment.failed": { chargeId: string; reason: string };
  "refund.created": { refundId: string; amount: number };
};

type EventName = keyof PayloadMap;

type WebhookHandler<E extends EventName> = (payload: PayloadMap[E]) => void;

const onPaymentSucceeded: WebhookHandler<"payment.succeeded"> = (payload) => {
  console.log(payload.chargeId, payload.amount);
};

const onRefundCreated: WebhookHandler<"refund.created"> = (payload) => {
  console.log(payload.chargeId);
  // Ошибка компиляции:
  // Property 'chargeId' does not exist on type '{ refundId: string; amount: number; }'
};
