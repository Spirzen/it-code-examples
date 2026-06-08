import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 200)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label="sin")
plt.plot(x, y2, label="cos")
plt.fill_between(x, y1, y2, alpha=0.25, color="steelblue")
plt.legend()
plt.title("Заливка между двумя сериями")
plt.grid(True, alpha=0.3)
plt.show()
