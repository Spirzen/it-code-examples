const WebhookEvent = {
  PaymentSucceeded: "payment.succeeded",
  PaymentFailed: "payment.failed",
  RefundCreated: "refund.created",
} as const;

type WebhookEventType = (typeof WebhookEvent)[keyof typeof WebhookEvent];
// "payment.succeeded" | "payment.failed" | "refund.created"

type PayloadMap = {
  [WebhookEvent.PaymentSucceeded]: { chargeId: string; amount: number };
  [WebhookEvent.PaymentFailed]: { chargeId: string; reason: string };
  [WebhookEvent.RefundCreated]: { refundId: string; amount: number };
};

type WebhookHandler<E extends WebhookEventType> = (
  payload: PayloadMap[E],
) => void;

const onPaymentSucceeded: WebhookHandler<"payment.succeeded"> = (payload) => {
  console.log(payload.chargeId, payload.amount);
};

const onPaymentFailed: WebhookHandler<"payment.failed"> = (payload) => {
  console.log(payload.chargeId, payload.reason);
};

const onRefundCreated: WebhookHandler<"refund.created"> = (payload) => {
  // console.log(payload.chargeId);
  // ошибка: Property 'chargeId' does not exist on RefundCreated payload
  console.log(payload.refundId, payload.amount);
};
