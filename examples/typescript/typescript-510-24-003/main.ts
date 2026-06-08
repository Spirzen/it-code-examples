type Entity = { id: string };

class InMemoryRepository<T extends Entity> {
  private items: T[] = [];

  add(item: T): void {
    this.items.push(item);
  }

  findById(id: string): T | undefined {
    return this.items.find((i) => i.id === id);
  }

  list(): readonly T[] {
    return this.items;
  }
}

type User = Entity & { name: string };

const users = new InMemoryRepository<User>();
users.add({ id: "1", name: "Анна" });
