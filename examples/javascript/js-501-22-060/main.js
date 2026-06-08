const target = {
    message: "Привет",
    count: 0
};

const handler = {
    get(target, prop, receiver) {
        console.log(`Чтение свойства: ${prop}`);
        return Reflect.get(target, prop, receiver);
    },
    
    set(target, prop, value, receiver) {
        console.log(`Запись свойства ${prop} = ${value}`);
        return Reflect.set(target, prop, value, receiver);
    },
    
    has(target, prop) {
        console.log(`Проверка наличия: ${prop}`);
        return Reflect.has(target, prop);
    },
    
    deleteProperty(target, prop) {
        console.log(`Удаление свойства: ${prop}`);
        return Reflect.deleteProperty(target, prop);
    }
};

const proxy = new Proxy(target, handler);

proxy.message;        // "Чтение свойства: message"
proxy.count = 5;      // "Запись свойства count = 5"
"name" in proxy;      // "Проверка наличия: name"
delete proxy.message; // "Удаление свойства: message"
