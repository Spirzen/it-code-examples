const calculator = {
    value: 0,
    add: function(num) {
        this.value += num;
        return this;
    },
    multiply: function(num) {
        this.value *= num;
        return this;
    },
    getResult: () => {
        return this.value; // this указывает не на calculator
    }
};

// Работает с обычными функциями
const result = calculator.add(5).multiply(3);
console.log(result.value); // 15

// Не работает со стрелочной функцией
console.log(calculator.getResult()); // undefined
