# Антипаттерн — тяжёлая проверка здоровья
@app.get("/health/ready")
async def heavy_health_check():
    # Полное сканирование таблицы для проверки БД
    user_count = await db.fetchval("SELECT COUNT(*) FROM users")
    
    # Обращение ко всем зависимостям с полной загрузкой данных
    catalog = await catalog_service.fetch_full_catalog()
    prices = await pricing_service.fetch_all_prices()
    
    # Проверка доступности всех очередей
    for queue in ALL_QUEUES:
        await queue_service.get_detailed_stats(queue)
    
    return {
        "status": "healthy",
        "user_count": user_count,
        "catalog_size": len(catalog),
        "prices_count": len(prices)
    }
