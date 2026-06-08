
import logging

logger = logging.getLogger(__name__)

def process_transaction(transaction_id: str):
    logger.info("Starting transaction processing", extra={"transaction_id": transaction_id})
    
    try:
        # Логика обработки
        result = _perform_operations(transaction_id)
        logger.info("Transaction processed successfully", extra={
            "transaction_id": transaction_id,
            "result": result
        })
        return result
    except Exception as e:
        logger.exception("Transaction processing failed", extra={
            "transaction_id": transaction_id,
            "error_type": type(e).__name__
        })
        raise
