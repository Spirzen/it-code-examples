import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 6, 150)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(x, y, color="#2a9d8f", linewidth=2.5)
ax.set(xlabel="x", ylabel="sin(x)", title="OO-стиль: fig и ax")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(True, axis="y", alpha=0.4)
fig.tight_layout()
plt.show()
