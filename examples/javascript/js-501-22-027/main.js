const component = "значение с пробелами и / символами";
console.log(encodeURIComponent(component));
// "значение%20с%20пробелами%20и%20%2F%20символами"

// Используется для кодирования параметров запроса
const params = {
    name: "Иван Петров",
    city: "Москва/Санкт-Петербург"
};

const queryString = Object.entries(params)
    .map(([key, value]) => 
`${encodeURIComponent(key)}=${encodeURIComponent(value)}`
    )
    .join("&");

console.log(queryString);
// "name=%D0%98%D0%B2%D0%B0%D0%BD%20%D0%9F%D0%B5%D1%82%D1%80%D0%BE%D0%B2&city=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2F%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3"
