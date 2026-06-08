interface Repository<T extends { id: string }> {
  findById(id: string): Promise<T | null>;
  save(entity: T): Promise<void>;
}

class InMemoryUserRepo implements Repository<User> {
  private store = new Map<string, User>();

  async findById(id: string): Promise<User | null> {
    return this.store.get(id) ?? null;
  }

  async save(entity: User): Promise<void> {
    this.store.set(entity.id, entity);
  }
}
