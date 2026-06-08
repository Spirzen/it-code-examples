
import time

def timer_decorator(func):
    """Декоратор для измерения времени выполнения функции"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Функция {func.__name__} выполнилась за {duration:.4f} сек.")
        return result
    return wrapper

@timer_decorator
def slow_function(n):
    time.sleep(n)
    return n * 2

if __name__ == "__main__":
    slow_function(2)
