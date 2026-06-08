const obj = {
    name: "Bob",
    regular: function() {
        console.log(this.name); // Bob
        setTimeout(function() {
            console.log(this.name); // undefined (this = window)
        }, 100);
    },
    arrow: function() {
        console.log(this.name); // Bob
        setTimeout(() => {
            console.log(this.name); // Bob (стрелочная функция унаследовала this)
        }, 100);
    }
};
