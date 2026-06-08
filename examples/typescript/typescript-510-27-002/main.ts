type Option<T> = { tag: "some"; value: T } | { tag: "none" };

function findById<T extends { id: string }>(
  items: T[],
  id: string,
): Option<T> {
  const item = items.find((i) => i.id === id);
  return item ? { tag: "some", value: item } : { tag: "none" };
}

function getName(items: User[], id: string): string {
  const found = findById(items, id);
  return found.tag === "some" ? found.value.name : "Гость";
}
