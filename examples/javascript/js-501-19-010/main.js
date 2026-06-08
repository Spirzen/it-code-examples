class Counter {
    constructor(startValue) {
        this.count = startValue;
    }

    increment() {
        this.count++;
        return this.count;
    }
    
    // Стрелочная функция в классе (редко используется для методов, если нужен динамический this)
    // Здесь this будет указывать на экземпляр класса, так как класс объявлен в глобальной области
    getCount = () => {
        return this.count;
    }
}

const counter = new Counter(10);

// Обычный метод
console.log(counter.increment()); // 11

// Привязка метода (если передать метод как callback)
const callback = counter.increment;
callback(); // Ошибка в strict mode: Cannot read properties of undefined (count)
// Это происходит потому, что при вызове callback() this становится undefined.

// Правильное использование стрелочного метода (классового поля)
console.log(counter.getCount()); // 11 (работает всегда, так как this захвачен при создании экземпляра)
