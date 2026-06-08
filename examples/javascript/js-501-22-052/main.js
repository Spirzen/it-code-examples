// Создание кастомного итератора
const range = {
    from: 1,
    to: 5,
    
    [Symbol.iterator]() {
        let current = this.from;
        const last = this.to;
        
        return {
            next() {
                if (current <= last) {
                    return { value: current++, done: false };
                } else {
                    return { done: true };
                }
            }
        };
    }
};

// Использование итератора
for (let num of range) {
    console.log(num); // 1, 2, 3, 4, 5
}

// Распространение в массив
const arr = [...range];
console.log(arr); // [1, 2, 3, 4, 5]
