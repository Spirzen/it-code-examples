const { isValidEmail } = require('./validators');

describe('isValidEmail', () => {
  test('принимает корректный email', () => {
    expect(isValidEmail('qa@example.com')).toBe(true);
  });

  test('отклоняет пустую строку', () => {
    expect(isValidEmail('')).toBe(false);
  });

  test('отклоняет строку без @', () => {
    expect(isValidEmail('not-an-email')).toBe(false);
  });
});
