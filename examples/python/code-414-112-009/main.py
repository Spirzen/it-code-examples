
import os
import signal
import sys

def spawn_worker():
    pid = os.fork()
    if pid == 0:
        # Дочерний процесс
        do_work()
        sys.exit(0)
    return pid

def handle_sigchld(signum, frame):
    # Сбор всех завершённых дочерних процессов
    while True:
        try:
            pid, status = os.waitpid(-1, os.WNOHANG)
            if pid == 0:
                break
            print(f"Дочерний процесс {pid} завершён со статусом {status}")
        except ChildProcessError:
            break

# Регистрация обработчика сигнала SIGCHLD
signal.signal(signal.SIGCHLD, handle_sigchld)
