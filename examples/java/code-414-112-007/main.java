// Потоковая обработка больших результатов
public void processAllOrders(Consumer<Order> processor) {
    int batchSize = 1000;
    long lastId = 0;
    
    while (true) {
        List<Order> batch = jdbcTemplate.query(
            "SELECT * FROM orders WHERE id > ? ORDER BY id LIMIT ?",
            new Object[]{lastId, batchSize},
            new OrderRowMapper()
        );
        
        if (batch.isEmpty()) {
            break;
        }
        
        batch.forEach(processor);
        lastId = batch.get(batch.size() - 1).getId();
        
        // Короткая пауза для снижения нагрузки на БД
        Thread.sleep(100);
    }
}
