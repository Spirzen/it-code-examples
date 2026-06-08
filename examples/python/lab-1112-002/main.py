import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

plt.plot(x, y, color="steelblue", linewidth=2, label="sin(x)")
plt.axhline(0, color="gray", linewidth=0.8)
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("Синусоида")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
