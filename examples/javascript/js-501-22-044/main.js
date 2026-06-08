const buffer = new ArrayBuffer(16);
const view = new DataView(buffer);

// Запись данных разных типов
view.setInt8(0, 127);           // 1 байт
view.setInt16(1, 32767);        // 2 байта
view.setInt32(3, 2147483647);   // 4 байта
view.setFloat32(7, 3.14);       // 4 байта
view.setFloat64(11, 2.71828);   // 8 байт

// Чтение данных
console.log(view.getInt8(0));        // 127
console.log(view.getInt16(1));       // 32767
console.log(view.getInt32(3));       // 2147483647
console.log(view.getFloat32(7));     // 3.14
console.log(view.getFloat64(11));    // 2.71828
