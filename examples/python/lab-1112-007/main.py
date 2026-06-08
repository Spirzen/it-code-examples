import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

fig, axes = plt.subplots(2, 2, figsize=(9, 7))
fig.suptitle("Панель из четырёх графиков")

axes[0, 0].plot(x, np.sin(x))
axes[0, 0].set_title("sin(x)")

axes[0, 1].plot(x, np.cos(x), color="orange")
axes[0, 1].set_title("cos(x)")

axes[1, 0].scatter(x[::5], np.random.default_rng(1).normal(size=20))
axes[1, 0].set_title("Scatter")

axes[1, 1].hist(np.random.default_rng(2).normal(size=300), bins=20)
axes[1, 1].set_title("Гистограмма")

fig.tight_layout()
plt.show()
