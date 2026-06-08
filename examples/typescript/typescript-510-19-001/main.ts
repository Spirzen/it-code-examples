interface User {
  id: string;
  name: string;
}

const byId = new Map<string, User>();
byId.set("u1", { id: "u1", name: "Ann" });

function getOrThrow(map: Map<string, User>, id: string): User {
  const user = map.get(id);
  if (!user) throw new Error(`User not found: ${id}`);
  return user;
}

const uniqueTags = new Set<string>(["ts", "ts", "js"]);
uniqueTags.add("node");
