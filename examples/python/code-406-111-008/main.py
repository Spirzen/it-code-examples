
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def process_order(order):
    logger.info(f"Начало обработки заказа {order.id}")
    
    try:
        logger.debug(f"Данные заказа: {order}")
        validate_order(order)
        save_order(order)
        logger.info(f"Заказ {order.id} успешно обработан")
    except ValidationError as ex:
        logger.warning(f"Ошибка валидации заказа {order.id}: {ex}")
        raise
    except Exception as ex:
        logger.error(f"Критическая ошибка при обработке заказа {order.id}", exc_info=True)
        raise
