
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            print("изменён:", event.src_path)

    def on_created(self, event):
        print("создан:", event.src_path)

    def on_deleted(self, event):
        print("удалён:", event.src_path)

observer = Observer()
observer.schedule(Handler(), path="./watched", recursive=True)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
