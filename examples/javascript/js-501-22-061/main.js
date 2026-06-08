const validator = {
    set(obj, prop, value) {
        if (prop === "age") {
            if (typeof value !== "number" || value < 0 || value > 150) {
                throw new RangeError("Возраст должен быть от 0 до 150");
            }
        }
        if (prop === "email") {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(value)) {
                throw new TypeError("Некорректный формат email");
            }
        }
        return Reflect.set(obj, prop, value);
    }
};

const user = new Proxy({}, validator);
user.age = 25;           // OK
user.email = "test@example.com"; // OK
// user.age = 200;       // RangeError
// user.email = "invalid"; // TypeError
