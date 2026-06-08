type User = { id: string; name: string };

async function fetchUser(id: string): Promise<User> {
  const res = await fetch(`/api/users/${id}`);
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  const raw: unknown = await res.json();
  if (!isUser(raw)) throw new Error("Invalid user JSON");
  return raw;
}

function isUser(value: unknown): value is User {
  if (typeof value !== "object" || value === null) return false;
  const o = value as Record<string, unknown>;
  return typeof o.id === "string" && typeof o.name === "string";
}
