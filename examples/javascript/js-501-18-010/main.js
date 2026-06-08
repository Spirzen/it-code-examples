const obj1 = { name: "Джон" };
const obj2 = { name: "Джон" };
const obj3 = obj1;

console.log(obj1 === obj2); // false - разные объекты
console.log(obj1 === obj3); // true - одна и та же ссылка

// Для сравнения по содержимому нужна специальная функция
function areEqual(objA, objB) {
    const keysA = Object.keys(objA);
    const keysB = Object.keys(objB);
    
    if (keysA.length !== keysB.length) {
        return false;
    }
    
    for (const key of keysA) {
        if (objA[key] !== objB[key]) {
            return false;
        }
    }
    
    return true;
}

console.log(areEqual(obj1, obj2)); // true - содержимое одинаковое
