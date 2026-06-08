# Псевдокод asyncio
async def main():
    task_a = download_async("https://example.com/a.zip")
    task_b = download_async("https://example.com/b.zip")
    data_a, data_b = await gather(task_a, task_b)
    # Оба запроса шли параллельно по сети → ~3 сек
    show("Готово")
