class UserFactory {
    static #userCount = 0;
    
    static createUser(type, name, email) {
        this.#userCount++;
        
        switch(type) {
            case 'admin':
                return new AdminUser(name, email, this.#userCount);
            case 'guest':
                return new GuestUser(name, email, this.#userCount);
            default:
                return new RegularUser(name, email, this.#userCount);
        }
    }
    
    static getUserCount() {
        return this.#userCount;
    }
}

class BaseUser {
    constructor(name, email, id) {
        this.name = name;
        this.email = email;
        this.id = id;
        this.createdAt = new Date();
    }
    
    getInfo() {
        return `${this.name} (${this.email})`;
    }
}

class AdminUser extends BaseUser {
    #permissions = ['read', 'write', 'delete', 'admin'];
    
    hasPermission(permission) {
        return this.#permissions.includes(permission);
    }
    
    getRole() {
        return 'Administrator';
    }
}

class GuestUser extends BaseUser {
    #permissions = ['read'];
    
    hasPermission(permission) {
        return this.#permissions.includes(permission);
    }
    
    getRole() {
        return 'Guest';
    }
}

class RegularUser extends BaseUser {
    #permissions = ['read', 'write'];
    
    hasPermission(permission) {
        return this.#permissions.includes(permission);
    }
    
    getRole() {
        return 'User';
    }
}

const admin = UserFactory.createUser('admin', 'Админ', 'admin@example.com');
const guest = UserFactory.createUser('guest', 'Гость', 'guest@example.com');
const user = UserFactory.createUser('user', 'Пользователь', 'user@example.com');

console.log(`Создано пользователей: ${UserFactory.getUserCount()}`);
console.log(`${admin.getInfo()} - ${admin.getRole()}`);
console.log(`${guest.getInfo()} - ${guest.getRole()}`);
console.log(`${user.getInfo()} - ${user.getRole()}`);
