function outerFunction() {
    let outerVar = "внешняя";
    
    function innerFunction() {
        let innerVar = "внутренняя";
        console.log(outerVar); // "внешняя"
        console.log(innerVar); // "внутренняя"
    }
    
    innerFunction();
    console.log(outerVar); // "внешняя"
    // console.log(innerVar); // ReferenceError
}

outerFunction();
