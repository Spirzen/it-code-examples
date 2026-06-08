class Counter {
  count = 0;

  // Обычный метод — свой this
  increment() {
    this.count += 1;
  }

  // Стрелка как поле — this зафиксирован на экземпляре
  incrementBound = () => {
    this.count += 1;
  };
}

const c = new Counter();
const fn = c.increment;
// fn(); // в strict JS/TS — this может быть undefined

const bound = c.incrementBound;
bound(); // OK: count увеличится
