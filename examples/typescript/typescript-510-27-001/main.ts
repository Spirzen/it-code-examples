type Result<T, E = string> =
  | { ok: true; value: T }
  | { ok: false; error: E };

function parseAge(input: string): Result<number, "nan" | "negative"> {
  const value = Number(input);
  if (Number.isNaN(value)) return { ok: false, error: "nan" };
  if (value < 0) return { ok: false, error: "negative" };
  return { ok: true, value };
}

function displayAge(input: string): string {
  const r = parseAge(input);
  if (!r.ok) {
    return r.error === "nan" ? "Введите число" : "Возраст не может быть отрицательным";
  }
  return `Возраст: ${r.value}`;
}
