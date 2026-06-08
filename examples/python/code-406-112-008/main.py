def process_order(order):
    logger.debug(f"Вход в process_order, order_id: {order.id}")
    
    try:
        logger.debug("Валидация заказа")
        validate_order(order)
        
        logger.debug("Сохранение заказа в БД")
        save_to_database(order)
        
        logger.debug("Отправка уведомления")
        send_notification(order)
        
        logger.debug(f"Выход из process_order, order_id: {order.id}")
    except Exception as ex:
        logger.error(f"Ошибка в process_order, order_id: {order.id}", exc_info=True)
        raise
