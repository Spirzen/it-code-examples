class AsyncResource {
    async open() {
        this.resource = await allocateResourceAsync();
    }
    
    async use() {
        console.log("Использую асинхронный ресурс");
    }
    
    async disposeAsync() {
        console.log("Освобождаю асинхронный ресурс");
        await freeResourceAsync(this.resource);
    }
}

// Использование
await using (const resource = new AsyncResource()) {
    await resource.open();
    await resource.use();
}
// disposeAsync вызван автоматически
