const obj = {
    value: 42,
    
    // Обычная функция
    regularMethod() {
        setTimeout(function() {
            // this здесь будет зависеть от того, как вызван setTimeout
            // В данном случае это window/global (или undefined в strict), так как функция вызвана как callback
            console.log('Regular callback this:', this?.value); 
        }, 100);
    },
    
    // Стрелочная функция
    arrowMethod() {
        setTimeout(() => {
            // this здесь наследуется из arrowMethod, который был вызван через obj.
            // Следовательно, this === obj
            console.log('Arrow callback this:', this.value); 
        }, 100);
    }
};

obj.regularMethod(); // Выведет undefined (или значение window.value)
obj.arrowMethod();   // Выведет 42
