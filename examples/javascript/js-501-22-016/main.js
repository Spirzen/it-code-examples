const obj = {};

Object.defineProperties(obj, {
    name: {
        value: "Тест",
        writable: true,
        enumerable: true,
        configurable: true
    },
    id: {
        value: 1,
        writable: false,
        enumerable: false,
        configurable: false
    }
});
