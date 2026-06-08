function toMessage(error: unknown): string {
  if (error instanceof Error) return error.message;
  if (typeof error === "string") return error;
  return "Неизвестная ошибка";
}

async function load(): Promise<Result<string, "network">> {
  try {
    const res = await fetch("/api/data");
    if (!res.ok) return { ok: false, error: "network" };
    return { ok: true, value: await res.text() };
  } catch (e: unknown) {
    console.error(toMessage(e));
    return { ok: false, error: "network" };
  }
}
