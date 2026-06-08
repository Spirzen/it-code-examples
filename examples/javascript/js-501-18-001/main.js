const user = {
  firstName: "Тимур",
  lastName: "Тагиров",
  
  // Обычный метод (ES5 и ES6+)
  getFullName: function() {
    return `${this.firstName} ${this.lastName}`;
  },

  // Краткая запись метода (ES6+) — рекомендуется для простоты
  greet() {
    return `Привет, я ${this.getFullName()}`;
  }
};

console.log(user.greet()); // Привет, я Тимур Тагиров
