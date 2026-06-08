function Person(firstName, lastName, age) {
  this.firstName = firstName;
  this.lastName = lastName;
  this.age = age;
}

const users = [
  new Person('John', 'Smith', 28),
  new Person('Jane', 'Doe', 31),
  new Person('Marko', 'Denic', 26)
];

console.log('Обычный лог');
console.info('Информационное сообщение');
console.warn('Предупреждение: поле age скоро станет обязательным');
console.error('Ошибка: не удалось загрузить профиль');

console.table(users);
console.table(users, ['firstName', 'age']); // только нужные колонки

console.group('Проверка пользователя');
console.log('id:', 42);
console.log('role:', 'admin');
console.groupEnd();

console.time('fetchUsers');
// ... тут любой код / await fetch(...)
console.timeEnd('fetchUsers'); // fetchUsers: 12.37ms

const isEmailValid = false;
console.assert(isEmailValid, 'Email должен быть валидным');
