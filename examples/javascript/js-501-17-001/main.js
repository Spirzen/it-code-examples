// --- Пример с var ---
function testVar() {
  if (true) {
    var x = 10; // Объявлена в области видимости функции testVar, а не блока if
  }
  console.log(x); // Выведет: 10 (доступна снаружи блока if)
}

testVar();

// --- Пример с let ---
function testLet() {
  if (true) {
    let y = 20; // Объявлена только внутри блока if
  }
  // console.log(y); // ОШИБКА: ReferenceError: y is not defined
  // Переменная y недоступна за пределами блока if
}

testLet();
