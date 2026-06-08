abstract class Repository<T extends { id: string }> {
  abstract findById(id: string): Promise<T | null>;

  protected log(message: string): void {
    console.log(`[repo] ${message}`);
  }

  async mustFindById(id: string): Promise<T> {
    const item = await this.findById(id);
    if (!item) throw new Error(`Not found: ${id}`);
    return item;
  }
}

class UserRepo extends Repository<{ id: string; name: string }> {
  async findById(id: string) {
    this.log(`find ${id}`);
    return { id, name: "Demo" };
  }
}
