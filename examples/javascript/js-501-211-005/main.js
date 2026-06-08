const map = [
  [1, 0, 1],
  [0, 0, 0],
  [1, 0, 1]
];

// Получение значения ячейки
const cellValue = map[1][2]; // 0

// Обход всей карты
for (let row of map) {
  for (let cell of row) {
    console.log(cell);
  }
}
