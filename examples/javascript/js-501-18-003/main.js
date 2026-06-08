class Person {
  constructor(firstName, lastName) {
    this.firstName = firstName;
    this.lastName = lastName;
  }

  // Метод класса (по умолчанию является статическим или instance методом)
  getFullName() {
    return `${this.firstName} ${this.lastName}`;
  }

  static createGuest(guestName) {
    return new Person(guestName, "Гость");
  }
}

const person = new Person("Анна", "Иванова");
console.log(person.getFullName()); // Анна Иванова

const guest = Person.createGuest("Борис");
console.log(guest.getFullName()); // Борис Гость
