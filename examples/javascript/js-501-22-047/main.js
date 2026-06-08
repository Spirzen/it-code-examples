const data = {
    title: "Продукт",
    price: 1999,
    inStock: true,
    tags: ["новинка", "акция"]
};

// Без форматирования
console.log(JSON.stringify(data));
// {"title":"Продукт","price":1999,"inStock":true,"tags":["новинка","акция"]}

// С отступами (2 пробела)
console.log(JSON.stringify(data, null, 2));
/*
{
  "title": "Продукт",
  "price": 1999,
  "inStock": true,
  "tags": [
    "новинка",
    "акция"
  ]
}
*/

// С табуляцией
console.log(JSON.stringify(data, null, "\t"));
