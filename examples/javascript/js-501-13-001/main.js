// так выглядит однострочный комментарий
/*
а вот так – 
многострочный комментарий
*/

// 1. Импорты

import { func } from './module.js';

// 2. Константы и настройки
const API_URL = "https://api.example.com";

// 3. Основные функции
function fetchData(url) {
  // ... логика загрузки данных
}

// 4. Обработчики событий для соответствующих объектов
document.getElementById("btn").addEventListener("click", () => {
  fetchData(API_URL);
});

// 5. Инициализация (запуск кода после загрузки страницы)
document.addEventListener("DOMContentLoaded", () => {
  console.log("Страница загружена!");
});
