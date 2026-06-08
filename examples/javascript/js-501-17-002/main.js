function example() {
    console.log(a); // undefined
    var a = 1;
    
    console.log(b); // ReferenceError
    let b = 2;
    
    console.log(c()); // 3
    function c() {
        return 3;
    }
}

example();
