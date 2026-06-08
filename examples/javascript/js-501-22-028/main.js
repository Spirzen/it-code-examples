const encodedComponent = "значение%20с%20пробелами%20и%20%2F%20символами";
console.log(decodeURIComponent(encodedComponent));
// "значение с пробелами и / символами"

// Пример декодирования параметров
const url = "https://example.com/?name=%D0%98%D0%B2%D0%B0%D0%BD&city=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0";
const paramsString = url.split("?")[1];
const paramsArray = paramsString.split("&");

const params = {};
paramsArray.forEach(param => {
    const [key, value] = param.split("=");
    params[decodeURIComponent(key)] = decodeURIComponent(value);
});

console.log(params);
// { name: "Иван", city: "Москва" }
