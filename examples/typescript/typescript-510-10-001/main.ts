function fail(message: string): never {
  throw new Error(message);
}

function parseUser(raw: unknown): { id: string; name: string } {
  if (typeof raw !== "object" || raw === null) {
    throw new Error("Expected object");
  }
  const o = raw as Record<string, unknown>;
  if (typeof o.id !== "string" || typeof o.name !== "string") {
    throw new Error("Invalid user shape");
  }
  return { id: o.id, name: o.name };
}
