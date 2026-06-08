let globalVar = "I am global";

function outer() {
    let outerVar = "I am outer";
    
    function inner() {
        let innerVar = "I am inner";
        
        // Разрешение имен по цепочке:
        // 1. innerVar -> найден внутри inner
        // 2. outerVar -> не найден в inner, найден в outer
        // 3. globalVar -> не найден в inner/outer, найден в глобальной
        
        console.log(innerVar);   // "I am inner"
        console.log(outerVar);   // "I am outer"
        console.log(globalVar);  // "I am global"
    }
    
    inner();
}

outer();
