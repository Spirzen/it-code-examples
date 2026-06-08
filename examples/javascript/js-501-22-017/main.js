const obj = { name: "Тест" };

// Запрещает добавление новых свойств
Object.preventExtensions(obj);
obj.newProp = "value"; // Не сработает в строгом режиме

// Запрещает добавление и удаление свойств
const sealed = { name: "Тест" };
Object.seal(sealed);
sealed.newProp = "value"; // Не сработает
delete sealed.name; // Не сработает

// Полностью блокирует изменения
const frozen = { name: "Тест" };
Object.freeze(frozen);
frozen.name = "Новое"; // Не сработает
frozen.newProp = "value"; // Не сработает
delete frozen.name; // Не сработает
