const original = {
    name: "Джон",
    address: {
        city: "Москва",
        street: "Тверская"
    }
};

// Способ 1: structuredClone
const deepCopy1 = structuredClone(original);
deepCopy1.address.city = "Санкт-Петербург";

console.log(original.address.city); // "Москва" — оригинал не изменился
console.log(deepCopy1.address.city); // "Санкт-Петербург"

// Способ 2: через JSON (только JSON-совместимые значения)
const deepCopy2 = JSON.parse(JSON.stringify(original));
deepCopy2.address.city = "Казань";

// Способ 3: рекурсивная функция
function deepClone(obj) {
    if (obj === null || typeof obj !== 'object') {
        return obj;
    }
    
    if (Array.isArray(obj)) {
        return obj.map(item => deepClone(item));
    }
    
    const cloned = {};
    for (const key in obj) {
        if (obj.hasOwnProperty(key)) {
            cloned[key] = deepClone(obj[key]);
        }
    }
    return cloned;
}

const deepCopy3 = deepClone(original);
