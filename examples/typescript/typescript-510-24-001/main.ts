type Dimension = "length" | "mass";

type UnitDef = { base: Dimension; factor: number };

const REGISTRY = {
  m: { base: "length", factor: 1 },
  km: { base: "length", factor: 1000 },
  mi: { base: "length", factor: 1609.34 },
  g: { base: "mass", factor: 1 },
  kg: { base: "mass", factor: 1000 },
  lb: { base: "mass", factor: 453.592 },
} as const satisfies Record<string, UnitDef>;

type UnitKey = keyof typeof REGISTRY;

type Compat<F extends UnitKey> = {
  [P in UnitKey]: (typeof REGISTRY)[P]["base"] extends (typeof REGISTRY)[F]["base"]
    ? P
    : never;
}[UnitKey];

declare function convert<F extends UnitKey, T extends Compat<F>>(
  value: number,
  from: F,
  to: T,
): number;

// convert(10, "km", "mi");   // OK — обе length
// convert(10, "km", "kg");   // ошибка: kg не в Compat<"km">
