interface User {
  id: string;
  name: string;
  role: "admin" | "user";
}

// Union и narrowing
type Id = string | number;
function isString(x: Id): x is string {
  return typeof x === "string";
}

function formatId(id: Id): string {
  if (isString(id)) return id.toUpperCase();
  return id.toFixed(0);
}

// Utility
type PartialUser = Partial<Pick<User, "name">>;
type PublicUser = Omit<User, "role">;

// Generic
function first<T>(arr: T[]): T | undefined {
  return arr[0];
}

const admin = first<User>([{ id: "1", name: "Ann", role: "admin" }]);
