class QueryBuilder {
  private parts: string[] = [];

  select(fields: string[]): this {
    this.parts.push(`SELECT ${fields.join(", ")}`);
    return this;
  }

  from(table: string): this {
    this.parts.push(`FROM ${table}`);
    return this;
  }

  build(): string {
    return this.parts.join(" ");
  }
}
