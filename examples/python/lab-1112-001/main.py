import matplotlib.pyplot as plt
import numpy as np

# 1. Данные
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 2. Рисование
plt.plot(x, y)

# 3. Подписи (без них график «голый» — преподаватель снимет баллы)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Заголовок")
plt.grid(True)

# 4. Показ
plt.show()
