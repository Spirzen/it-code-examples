type Constructor<T = object> = new (...args: unknown[]) => T;

function Timestamped<TBase extends Constructor>(Base: TBase) {
  return class extends Base {
    readonly createdAt = new Date();
  };
}

function Identifiable<TBase extends Constructor<{ id?: string }>>(Base: TBase) {
  return class extends Base {
    constructor(...args: unknown[]) {
      super(...args);
      if (!("id" in this) || !this.id) {
        (this as { id: string }).id = crypto.randomUUID();
      }
    }
  };
}

class User {
  constructor(public name: string) {}
}

const UserEntity = Timestamped(Identifiable(User));

const u = new UserEntity("Анна");
console.log(u.name, u.id, u.createdAt);
