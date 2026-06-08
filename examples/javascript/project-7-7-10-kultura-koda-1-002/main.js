/**
 * Пользователь системы.
 * @param {string} name
 * @param {number} age
 */
function User(name, age) {
    this.name = name;
    this.age = age;
}

/**
 * @returns {boolean}
 */
User.prototype.isAdult = function () {
    return this.age >= 18;
};
