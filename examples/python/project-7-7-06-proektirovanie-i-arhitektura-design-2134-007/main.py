from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task(bind=True, max_retries=3, time_limit=300)
def generate_report(self, user_id, parameters):
    """Генерация отчёта в фоновом режиме."""
    try:
        # Долгая операция выполняется вне основного потока
        data = fetch_large_dataset(user_id, parameters)
        report = process_data(data)
        store_report(user_id, report)
        notify_user(user_id, "Отчёт готов")
    except Exception as exc:
        # Автоматический перезапуск при сбоях
        raise self.retry(exc=exc, countdown=60)
