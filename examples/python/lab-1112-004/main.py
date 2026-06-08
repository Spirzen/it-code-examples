import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 300)

plt.plot(x, np.sin(x), label="sin(x)")
plt.plot(x, np.cos(x), label="cos(x)", linestyle="--")
plt.plot(x, np.sin(x) * np.exp(-0.1 * x), label="затухающая sin")
plt.legend()
plt.grid(True, alpha=0.3)
plt.title("Сравнение функций")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
