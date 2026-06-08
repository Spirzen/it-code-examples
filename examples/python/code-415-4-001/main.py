import sys

a = []
b = [a]
a.append(b)  # refcount > 0 у обоих, снаружи недостижимы
del a, b
import gc
gc.collect()  # разрывает цикл
