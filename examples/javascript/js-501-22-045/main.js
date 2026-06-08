const sharedBuffer = new SharedArrayBuffer(1024);
const sharedArray = new Int32Array(sharedBuffer);

// Атомарная запись
Atomics.store(sharedArray, 0, 100);
console.log(Atomics.load(sharedArray, 0)); // 100

// Атомарное сложение
Atomics.add(sharedArray, 0, 50);
console.log(Atomics.load(sharedArray, 0)); // 150

// Атомарное вычитание
Atomics.sub(sharedArray, 0, 30);
console.log(Atomics.load(sharedArray, 0)); // 120

// Атомарное сравнение и замена
Atomics.compareExchange(sharedArray, 0, 120, 200);
console.log(Atomics.load(sharedArray, 0)); // 200

// Атомарный инкремент
Atomics.add(sharedArray, 1, 1);
console.log(Atomics.load(sharedArray, 1)); // 1
