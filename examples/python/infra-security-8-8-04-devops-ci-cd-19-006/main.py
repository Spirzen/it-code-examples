# Опасный паттерн — логирование каждой итерации
def synchronize_catalog(external_api, local_db):
    items = external_api.fetch_all_items()
    logger.info(f"Получено {len(items)} товаров для синхронизации")
    
    updated = 0
    created = 0
    errors = 0
    
    for item in items:
        try:
            logger.debug(f"Обработка товара: {item['sku']} - {item['name']}")
            
            existing = local_db.find_by_sku(item['sku'])
            if existing:
                local_db.update(existing, item)
                updated += 1
                logger.info(f"Обновлён товар: {item['sku']}")
            else:
                local_db.create(item)
                created += 1
                logger.info(f"Создан товар: {item['sku']}")
                
        except Exception as e:
            errors += 1
            logger.error(f"Ошибка обработки {item['sku']}: {e}")
    
    logger.info(
        f"Синхронизация завершена: "
        f"создано={created}, обновлено={updated}, ошибок={errors}"
    )
