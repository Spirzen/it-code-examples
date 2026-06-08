class ValidationError extends Error {
    constructor(message, field) {
        super(message);
        this.name = "ValidationError";
        this.field = field;
        this.timestamp = new Date().toISOString();
    }
}

class DatabaseError extends Error {
    constructor(message, query, code) {
        super(message);
        this.name = "DatabaseError";
        this.query = query;
        this.code = code;
        this.timestamp = new Date().toISOString();
    }
}

class AuthenticationError extends Error {
    constructor(message, userId = null) {
        super(message);
        this.name = "AuthenticationError";
        this.userId = userId;
        this.timestamp = new Date().toISOString();
    }
}

// Использование
function validateUser(user) {
    if (!user.name || user.name.length < 2) {
        throw new ValidationError("Имя должно содержать минимум 2 символа", "name");
    }
    
    if (!user.email || !user.email.includes("@")) {
        throw new ValidationError("Некорректный email", "email");
    }
    
    if (user.age < 0 || user.age > 150) {
        throw new ValidationError("Некорректный возраст", "age");
    }
    
    return true;
}

try {
    validateUser({ name: "А", email: "invalid", age: 200 });
} catch (error) {
    if (error instanceof ValidationError) {
        console.log(`${error.name}: ${error.message}`);
        console.log(`Поле: ${error.field}`);
        console.log(`Время: ${error.timestamp}`);
    }
}
