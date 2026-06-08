const user = {
    _name: "Анна",
    _age: 25,
    
    get name() {
        return this._name.toUpperCase();
    },
    
    set name(value) {
        if (value.length > 2) {
            this._name = value;
        }
    },
    
    get age() {
        return this._age;
    },
    
    set age(value) {
        if (value >= 0 && value <= 120) {
            this._age = value;
        }
    }
};

console.log(user.name); // "АННА"
user.name = "Петр";
console.log(user.name); // "ПЕТР"
