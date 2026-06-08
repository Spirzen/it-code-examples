const user = {
    name: "Bob",
    regularFunc: function() {
        console.log("Regular:", this.name); // "Bob" (this = user)
        
        const arrowFunc = () => {
            console.log("Arrow:", this.name); // "Bob" (this из parent)
        };
        arrowFunc();
    },
    arrowMethod: () => {
        console.log(this.name); // undefined (this = window)
    }
};

user.regularFunc(); // Regular: Bob, Arrow: Bob
user.arrowMethod(); // undefined
