const buffer = new ArrayBuffer(16);

// Создание представлений на буфер
const uint8View = new Uint8Array(buffer);
const uint16View = new Uint16Array(buffer);
const float32View = new Float32Array(buffer);

// Запись данных через одно представление
uint8View[0] = 255;
uint8View[1] = 128;
uint8View[2] = 64;
uint8View[3] = 32;

// Чтение через другое представление
console.log(uint16View[0]); // 32895
console.log(float32View[0]); // 1.539989614439558e-36
