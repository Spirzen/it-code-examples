import matplotlib.pyplot as plt
import numpy as np

matrix = np.array([
    [1.0, 0.8, 0.3, 0.1],
    [0.8, 1.0, 0.5, 0.2],
    [0.3, 0.5, 1.0, 0.7],
    [0.1, 0.2, 0.7, 1.0],
])

fig, ax = plt.subplots()
im = ax.imshow(matrix, cmap="RdYlBu_r", vmin=0, vmax=1)
ax.set_xticks(range(4))
ax.set_yticks(range(4))
ax.set_xticklabels(["F1", "F2", "F3", "F4"])
ax.set_yticklabels(["F1", "F2", "F3", "F4"])
fig.colorbar(im, ax=ax, label="Корреляция")
ax.set_title("Матрица корреляций")
plt.show()
