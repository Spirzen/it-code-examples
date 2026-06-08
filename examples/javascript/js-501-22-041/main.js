class DataValidator {
    static isValidNumber(value) {
        return !isNaN(parseFloat(value)) && isFinite(value);
    }
    
    static parseInteger(value, defaultValue = 0) {
        const parsed = parseInt(value, 10);
        return this.isValidNumber(parsed) ? parsed : defaultValue;
    }
    
    static parseFloat(value, defaultValue = 0.0) {
        const parsed = parseFloat(value);
        return this.isValidNumber(parsed) ? parsed : defaultValue;
    }
    
    static isValidURL(url) {
        try {
            new URL(url);
            return true;
        } catch {
            return false;
        }
    }
    
    static encodeURLParams(params) {
        return Object.entries(params)
            .map(([key, value]) => 
`${encodeURIComponent(key)}=${encodeURIComponent(value)}`
            )
            .join("&");
    }
    
    static decodeURLParams(queryString) {
        const params = {};
        queryString.split("&").forEach(param => {
            const [key, value] = param.split("=");
            params[decodeURIComponent(key)] = decodeURIComponent(value || "");
        });
        return params;
    }
}

// Использование
console.log(DataValidator.isValidNumber("123")); // true
console.log(DataValidator.isValidNumber("текст")); // false
console.log(DataValidator.parseInteger("42")); // 42
console.log(DataValidator.parseInteger("текст")); // 0

const urlParams = { name: "Иван Петров", city: "Москва" };
const encoded = DataValidator.encodeURLParams(urlParams);
console.log(encoded); // "name=%D0%98%D0%B2%D0%B0%D0%BD%20%D0%9F%D0%B5%D1%82%D1%80%D0%BE%D0%B2&city=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0"

const decoded = DataValidator.decodeURLParams(encoded);
console.log(decoded); // { name: "Иван Петров", city: "Москва" }
