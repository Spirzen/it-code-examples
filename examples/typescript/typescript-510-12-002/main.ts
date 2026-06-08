function assertNever(x: never): never {
  throw new Error(`Unexpected value: ${x}`);
}

type Shape = { kind: "circle"; r: number } | { kind: "square"; a: number };

function area(s: Shape): number {
  switch (s.kind) {
    case "circle":
      return Math.PI * s.r ** 2;
    case "square":
      return s.a ** 2;
    default:
      return assertNever(s);
  }
}
