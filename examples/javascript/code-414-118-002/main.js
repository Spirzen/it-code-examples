function registerUser(email, age) {
  if (email == null) {
    throw new Error("email обязателен");
  }
  if (typeof email !== "string") {
    throw new TypeError("email должен быть строкой");
  }
  if (!email.trim()) {
    throw new Error("email не может быть пустым");
  }

  if (typeof age !== "number" || !Number.isInteger(age)) {
    throw new TypeError("age должен быть целым числом");
  }
  if (age < 0 || age > 150) {
    throw new RangeError("age вне допустимого диапазона");
  }

  return { email: email.trim(), age };
}
