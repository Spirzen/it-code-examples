function makeImmutable(obj) {
    return new Proxy(obj, {
        set(target, prop, value) {
            throw new Error(`Нельзя изменить свойство ${prop}`);
        },
        deleteProperty(target, prop) {
            throw new Error(`Нельзя удалить свойство ${prop}`);
        }
    });
}

const config = makeImmutable({
    apiUrl: "https://api.example.com",
    timeout: 5000,
    debug: false
});

// config.apiUrl = "new-url"; // Error
// delete config.timeout;     // Error
