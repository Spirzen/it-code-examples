class Entity {
  constructor(public id: string) {}
}

class Product extends Entity {
  constructor(
    id: string,
    public title: string,
    public price: number,
  ) {
    super(id);
  }

  label(): string {
    return `${this.title} (${this.price})`;
  }
}
