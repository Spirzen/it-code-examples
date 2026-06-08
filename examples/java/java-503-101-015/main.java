// Плохо: исключение может быть потеряно
CompletableFuture.supplyAsync(() -> fetchData())
    .thenAccept(data -> processData(data));
// Если fetchData выбросит исключение, оно не будет обработано

// Хорошо: обработка ошибок
CompletableFuture.supplyAsync(() -> fetchData())
    .thenApply(data -> {
        processData(data);
        return data;
    })
    .exceptionally(ex -> {
        logger.error("Failed to process data", ex);
        return null;
    });
