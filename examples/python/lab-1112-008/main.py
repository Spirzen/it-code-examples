import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 13)
sales = [40, 45, 50, 48, 55, 60, 58, 62, 65, 70, 68, 75]
returns = [2, 3, 2, 4, 3, 5, 4, 3, 6, 5, 4, 7]

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))
ax1.plot(x, sales, marker="o")
ax1.set_ylabel("Продажи")
ax1.set_title("Продажи и возвраты по месяцам")
ax1.grid(True, alpha=0.3)

ax2.bar(x, returns, color="salmon")
ax2.set_xlabel("Месяц")
ax2.set_ylabel("Возвраты")

fig.tight_layout()
plt.show()
