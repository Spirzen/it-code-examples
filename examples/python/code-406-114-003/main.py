
import tracemalloc
import gc

# Включение трассировки выделения памяти
tracemalloc.start()

# Выполнение кода
# ...

# Снимок текущего состояния
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[ Top 10 memory allocations ]")
for stat in top_stats[:10]:
    print(stat)

# Принудительная сборка мусора
gc.collect()
