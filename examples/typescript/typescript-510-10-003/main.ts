type Payment = { id: string; amount: number };

function isPayment(value: unknown): value is Payment {
  if (typeof value !== "object" || value === null) return false;
  const o = value as Record<string, unknown>;
  return typeof o.id === "string" && typeof o.amount === "number";
}

function charge(raw: unknown): void {
  if (!isPayment(raw)) {
    throw new Error("Invalid payment payload");
  }
  console.log(raw.amount); // Payment, не unknown
}
