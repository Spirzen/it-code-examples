const { expect } = require('chai');
const { add } = require('../src/utils');

describe('Модуль утилит', () => {
  describe('Функция сложения', () => {
    it('должна возвращать сумму двух чисел', () => {
      const result = add(2, 3);
      expect(result).to.equal(5);
    });

    it('должна работать с отрицательными числами', () => {
      const result = add(-1, -1);
      expect(result).to.equal(-2);
    });
  });
});
