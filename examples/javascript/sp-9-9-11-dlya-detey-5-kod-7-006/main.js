document.getElementById("проверить").addEventListener("click", function() {
  let возраст = parseInt(document.getElementById("возраст").value);
  // parseInt — превращает строку "15" в число 15

  if (isNaN(возраст)) {
    // isNaN = is Not a Number
    document.getElementById("результатВозраста").textContent = "Введите число!";
  } else if (возраст < 6) {
    document.getElementById("результатВозраста").textContent = "Детский сад ждёт!";
  } else if (возраст < 12) {
    document.getElementById("результатВозраста").textContent = "Пора за парту!";
  } else {
    document.getElementById("результатВозраста").textContent = "Вы уже знаете JavaScript — это круто!";
  }
});
