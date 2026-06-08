import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(0)
data = [
    rng.normal(100, 10, 100),
    rng.normal(105, 12, 100),
    rng.normal(95, 8, 100),
]

plt.boxplot(data, tick_labels=["Группа A", "Группа B", "Группа C"])
plt.ylabel("Значение")
plt.title("Сравнение распределений")
plt.grid(True, axis="y", alpha=0.3)
plt.show()
