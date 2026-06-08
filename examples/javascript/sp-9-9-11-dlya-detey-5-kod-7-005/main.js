let кнопка = document.getElementById("приветствовать");
let полеИмени = document.getElementById("имя");
let полеОтвета = document.getElementById("ответ");

кнопка.addEventListener("click", function() {
  let введённоеИмя = полеИмени.value.trim(); // .trim() убирает пробелы по краям

  if (введённоеИмя === "") {
    полеОтвета.textContent = "Пожалуйста, введите имя.";
    полеОтвета.style.color = "red";
  } else {
    полеОтвета.textContent = "Привет, " + введённоеИмя + "! Рады Вас видеть.";
    полеОтвета.style.color = "green";
  }
});
