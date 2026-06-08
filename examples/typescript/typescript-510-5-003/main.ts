type User = { id: string; name: string };

type LoadState =
  | { status: "idle" }
  | { status: "loading" }
  | { status: "success"; data: User }
  | { status: "error"; message: string };

function isUser(v: unknown): v is User {
  if (typeof v !== "object" || v === null) return false;
  const o = v as Record<string, unknown>;
  return typeof o.id === "string" && typeof o.name === "string";
}

async function fetchUser(id: string): Promise<LoadState> {
  try {
    const res = await fetch(`/api/users/${id}`);
    if (!res.ok) {
      return { status: "error", message: `HTTP ${res.status}` };
    }
    const raw: unknown = await res.json();
    if (!isUser(raw)) {
      return { status: "error", message: "Invalid JSON shape" };
    }
    return { status: "success", data: raw };
  } catch (e: unknown) {
    return {
      status: "error",
      message: e instanceof Error ? e.message : "Network error",
    };
  }
}
