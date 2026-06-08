class CustomResource {
    constructor() {
        this.resource = allocateResource();
    }
    
    use() {
        // Работа с ресурсом
        console.log("Использую ресурс");
    }
    
    dispose() {
        // Освобождение ресурса
        console.log("Освобождаю ресурс");
        freeResource(this.resource);
    }
}

// Использование
using (const resource = new CustomResource()) {
    resource.use();
}
// dispose вызван автоматически
