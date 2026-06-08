// Глобальные переменные (доступны во всех функциях)
let загаданноеЧисло;
let попыток = 0;

// Функция инициализации игры
function начатьИгру() {
  загаданноеЧисло = Math.floor(Math.random() * 100) + 1; // от 1 до 100
  попыток = 0;
  document.getElementById("подсказка").textContent = "Число загадано! Попробуйте угадать.";
  document.getElementById("подсказка").style.color = "black";
  document.getElementById("счётчик").textContent = "Попыток: 0";
  document.getElementById("ввод").value = ""; // очистить поле
}

// Запуск игры при загрузке
начатьИгру();

// Обработчик кнопки "Отправить"
document.getElementById("отправить").addEventListener("click", function() {
  let введённоеЧисло = parseInt(document.getElementById("ввод").value);

  // Проверка корректности ввода
  if (isNaN(введённоеЧисло) || введённоеЧисло < 1 || введённоеЧисло > 100) {
    document.getElementById("подсказка").textContent = "Введите число от 1 до 100.";
    document.getElementById("подсказка").style.color = "orange";
    return; // прервать выполнение функции
  }

  попыток++;

  if (введённоеЧисло === загаданноеЧисло) {
    document.getElementById("подсказка").textContent = 
      "🎉 Поздравляем! Вы угадали число " + загаданноеЧисло + " за " + попыток + " попыток!";
    document.getElementById("подсказка").style.color = "green";
  } else if (введённоеЧисло < загаданноеЧисло) {
    document.getElementById("подсказка").textContent = "Загаданное число больше.";
    document.getElementById("подсказка").style.color = "blue";
  } else {
    document.getElementById("подсказка").textContent = "Загаданное число меньше.";
    document.getElementById("подсказка").style.color = "purple";
  }

  document.getElementById("счётчик").textContent = "Попыток: " + попыток;
});

// Обработчик кнопки "Новая игра"
document.getElementById("сбросить").addEventListener("click", начатьИгру);
