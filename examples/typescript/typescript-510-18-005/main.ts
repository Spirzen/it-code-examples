interface Serializable {
  toJSON(): string;
}

interface Timestamped {
  updatedAt: Date;
}

class Article implements Serializable, Timestamped {
  constructor(
    public title: string,
    public updatedAt: Date,
  ) {}

  toJSON(): string {
    return JSON.stringify({ title: this.title, updatedAt: this.updatedAt });
  }
}
