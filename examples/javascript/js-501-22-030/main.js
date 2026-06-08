const primitive = true;
const object = new Boolean(true);

console.log(typeof primitive); // "boolean"
console.log(typeof object); // "object"

console.log(primitive === true); // true
console.log(object === true); // false — объект не равен примитиву
console.log(object == true); // true — приведение типов

// Объект Boolean всегда истинен в логическом контексте
if (new Boolean(false)) {
    console.log("Это выполнится"); // Выполнится
}
