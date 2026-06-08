// Создание матрицы (пример структуры данных)
const grid = [
  [1, 0, 1],
  [0, 1, 0],
  [1, 0, 1]
];

// Доступ к элементу матрицы
const cellValue = grid[1][2]; // Значение 0
console.log("\nЗначение ячейки [1][2]:", cellValue);

// Флаттенинг (сплющивание) многомерного массива
const nestedArray = [[1, 2], [3, 4], [5, 6]];
const flatArray = nestedArray.flat(); // [1, 2, 3, 4, 5, 6]
console.log("Сплющенный массив:", flatArray);

// Использование flatMap (map + flat в одном шаге)
const words = ["hello", "world"];
// Преобразуем слова в массив символов и сплющиваем результат
const allChars = words.flatMap(word => word.split(''));
console.log("Все символы:", allChars);
