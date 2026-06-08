const registry = new FinalizationRegistry(heldValue => {
    console.log(`Объект освобождён: ${heldValue}`);
});

class Resource {
    constructor(name) {
        this.name = name;
        this.buffer = new ArrayBuffer(1024 * 1024); // 1 МБ
        registry.register(this, name, this);
    }
    
    cleanup() {
        registry.unregister(this);
        console.log(`Ресурс ${this.name} очищен вручную`);
    }
}

// Создание ресурса
const resource1 = new Resource("файл1");
const resource2 = new Resource("файл2");

// Удаление ссылок
resource1 = null;
resource2.cleanup();
resource2 = null;

// Через некоторое время в консоли:
// "Объект освобождён: файл1"
