class User {
    constructor(name, email) {
        this.name = name;
        this.email = email;
        this.createdAt = new Date();
    }
    
    getInfo() {
        return `${this.name} (${this.email})`;
    }
}

const user = new User("Анна", "anna@example.com");
console.log(user.getInfo()); // "Анна (anna@example.com)"
