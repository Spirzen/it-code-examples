interface Named {
  name: string;
}

class User implements Named {
  constructor(
    public readonly id: string,
    public name: string,
    private role: "admin" | "user",
  ) {}

  isAdmin(): boolean {
    return this.role === "admin";
  }
}

const u = new User("u-1", "Иван", "user");
console.log(u.name, u.isAdmin());
