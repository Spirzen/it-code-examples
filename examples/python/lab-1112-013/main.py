import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 300)
y = np.sin(x)
peak_idx = np.argmax(y)
peak_x, peak_y = x[peak_idx], y[peak_idx]

plt.plot(x, y)
plt.scatter([peak_x], [peak_y], color="red", zorder=5)
plt.annotate(
    f"max = {peak_y:.2f}",
    xy=(peak_x, peak_y),
    xytext=(peak_x + 1.5, peak_y - 0.3),
    arrowprops=dict(arrowstyle="->", color="gray"),
)
plt.title("Поиск и подпись экстремума")
plt.grid(True, alpha=0.3)
plt.show()
