"""
Сравнение sequential, threading, asyncio и multiprocessing на I/O и CPU задачах.
Практикум: https://spirzen.ru/encyclopedia/4-code-dev/4-05-asinhronnost/3
"""
import asyncio
import multiprocessing
import random
import sys
import threading
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

try:
    from tqdm import tqdm

    HAS_TQDM = True
except ImportError:
    HAS_TQDM = False
    print("Установите tqdm: pip install tqdm", file=sys.stderr)


# --- I/O-bound (симуляция сети) ---


def io_task(task_id, delay):
    time.sleep(delay)
    return f"IO-задача #{task_id} (задержка {delay:.2f}с)"


async def io_task_async(task_id, delay):
    await asyncio.sleep(delay)
    return f"IO-задача #{task_id} (задержка {delay:.2f}с)"


# --- CPU-bound (вычисления) ---


def cpu_task(task_id, size=5_000_000):
    result = 0
    for i in range(size):
        result += i * i
    return f"CPU-задача #{task_id} (вычислено {size} итераций)"


def run_sequential(tasks, task_type="io"):
    print(f"\n{'=' * 60}")
    print(f"ПОСЛЕДОВАТЕЛЬНЫЙ РЕЖИМ ({task_type.upper()})")
    print("=" * 60)

    start_time = time.time()
    results = []
    iterator = tqdm(tasks, desc="Выполнение", unit="задач") if HAS_TQDM else tasks

    for task_id, value in iterator:
        if task_type == "io":
            results.append(io_task(task_id, value))
        else:
            results.append(cpu_task(task_id, value))

    elapsed = time.time() - start_time
    print(f"\nПоследовательно: {elapsed:.2f} сек")
    return results, elapsed


def run_threads(tasks, max_workers=10):
    print(f"\n{'=' * 60}")
    print(f"ПОТОКИ — {len(tasks)} задач, {max_workers} воркеров")
    print("=" * 60)

    start_time = time.time()
    results = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(io_task if isinstance(delay, float) else cpu_task, task_id, delay)
            for task_id, delay in tasks
        ]
        iterator = tqdm(futures, desc="Выполнение", unit="задач") if HAS_TQDM else futures
        for future in iterator:
            results.append(future.result())

    elapsed = time.time() - start_time
    print(f"\nПотоки: {elapsed:.2f} сек")
    return results, elapsed


def run_processes(tasks, max_workers=None):
    if max_workers is None:
        max_workers = multiprocessing.cpu_count()

    print(f"\n{'=' * 60}")
    print(f"МНОГОПРОЦЕССОРНОСТЬ — {len(tasks)} задач, {max_workers} ядер")
    print("=" * 60)

    start_time = time.time()
    results = []

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(cpu_task, task_id, size) for task_id, size in tasks]
        iterator = tqdm(futures, desc="Выполнение", unit="задач") if HAS_TQDM else futures
        for future in iterator:
            results.append(future.result())

    elapsed = time.time() - start_time
    print(f"\nПроцессы: {elapsed:.2f} сек")
    return results, elapsed


async def run_async_io(tasks):
    print(f"\n{'=' * 60}")
    print(f"ASYNCIO — {len(tasks)} задач")
    print("=" * 60)

    start_time = time.time()
    async_tasks = [asyncio.create_task(io_task_async(task_id, delay)) for task_id, delay in tasks]

    if HAS_TQDM:
        results = []
        for i, task in enumerate(async_tasks, 1):
            results.append(await task)
            print(
                f"\rПрогресс: [{'#' * i}{'.' * (len(tasks) - i)}] {i}/{len(tasks)}",
                end="",
            )
        print()
    else:
        results = await asyncio.gather(*async_tasks)

    elapsed = time.time() - start_time
    print(f"\nАсинхронно: {elapsed:.2f} сек")
    return results, elapsed


def visualize_comparison(results_dict):
    print("\n" + "=" * 60)
    print("ВИЗУАЛИЗАЦИЯ РЕЗУЛЬТАТОВ")
    print("=" * 60)

    max_time = max(results_dict.values())
    sorted_results = sorted(results_dict.items(), key=lambda x: x[1])

    print("\nСравнение времени выполнения:\n")
    for name, time_val in sorted_results:
        bar_length = int((time_val / max_time) * 50)
        bar = "█" * bar_length + "░" * (50 - bar_length)
        best_marker = " (лучший)" if time_val == sorted_results[0][1] else ""
        print(f"{name:20} {bar} {time_val:6.2f} сек{best_marker}")

    if "sequential (IO)" in results_dict or "sequential (CPU)" in results_dict:
        base_key = next(k for k in results_dict if k.startswith("sequential"))
        base_time = results_dict[base_key]
        print(f"\nУскорение относительно {base_key}:")
        for name, time_val in sorted_results:
            if name != base_key:
                print(f"  {name}: {base_time / time_val:.2f}x")


def main():
    print("СРАВНЕНИЕ ПОДХОДОВ К ПАРАЛЛЕЛИЗМУ")
    print("=" * 60)

    print("\nI/O-BOUND (симуляция сети)")
    print("-" * 40)

    num_io_tasks = 15
    io_tasks = [(i, random.uniform(0.5, 2.0)) for i in range(num_io_tasks)]

    _, seq_io_time = run_sequential(io_tasks, "io")
    _, threads_io_time = run_threads(io_tasks, max_workers=8)
    _, async_io_time = asyncio.run(run_async_io(io_tasks))

    print("\n\nCPU-BOUND (интенсивные вычисления)")
    print("-" * 40)

    num_cpu_tasks = multiprocessing.cpu_count() * 2
    cpu_tasks = [(i, random.randint(3_000_000, 7_000_000)) for i in range(num_cpu_tasks)]

    _, seq_cpu_time = run_sequential(cpu_tasks, "cpu")
    _, proc_cpu_time = run_processes(cpu_tasks)

    print("\nВНИМАНИЕ: потоки для CPU из-за GIL почти не ускоряют!")
    _, threads_cpu_time = run_threads(cpu_tasks, max_workers=multiprocessing.cpu_count())

    io_compare = {
        "sequential (IO)": seq_io_time,
        "threads (IO)": threads_io_time,
        "async (IO)": async_io_time,
    }
    cpu_compare = {
        "sequential (CPU)": seq_cpu_time,
        "processes (CPU)": proc_cpu_time,
        "threads (CPU)": threads_cpu_time,
    }

    print("\nI/O задачи:")
    visualize_comparison(io_compare)
    print("\nCPU задачи:")
    visualize_comparison(cpu_compare)

    print(f"\nЯдер CPU: {multiprocessing.cpu_count()}")
    print(f"Задач I/O: {num_io_tasks}, CPU: {num_cpu_tasks}")


if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
