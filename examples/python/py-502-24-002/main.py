def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            result = func(*args, **kwargs)
            duration = time.time() - start
            logger.info(f"{func.__name__} завершена за {duration:.4f} сек")
            return result
        except Exception as e:
            duration = time.time() - start
            logger.error(f"{func.__name__} завершена с ошибкой за {duration:.4f} сек: {e}")
            raise
    return wrapper
