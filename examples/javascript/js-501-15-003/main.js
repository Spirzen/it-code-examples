const jedi = {
    name: "Оби-Ван Кеноби",
    sayName: function() {
        // Обычная функция создает свой контекст
        setTimeout(function() {
            console.log(this.name); // undefined (this указывает на window)
        }, 1000);
        
        // Стрелочная функция сохраняет контекст
        setTimeout(() => {
            console.log(this.name); // "Оби-Ван Кеноби"
        }, 1000);
    }
};

jedi.sayName();
