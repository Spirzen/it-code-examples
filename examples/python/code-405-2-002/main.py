# Псевдокод threading
results = {}
def worker(url, key):
    results[key] = download(url)  # блокирующий вызов

start_thread(worker, url_a, "a")
start_thread(worker, url_b, "b")
wait_all_threads()
show("Готово")
